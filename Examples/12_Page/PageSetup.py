from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/Wikipedia_Science.png"
inputFile2 = "./Demos/Data/Summary_of_Science.txt"
outputFile = "PageSetup.pdf"

def ReadFromTxt(fname: str) -> str:
    with open(fname, 'r') as f:
        text = f.read()
    return text

def DrawPage(page):
    pageWidth = page.Canvas.ClientSize.Width
    y = 0.0
    # Title
    y = y + 5
    brush2 = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
    font2 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
    format2 = PdfStringFormat(PdfTextAlignment.Center)
    format2.CharacterSpacing = 1.0
    text = "Summary of Science"
    page.Canvas.DrawString(text, font2, brush2, pageWidth / 2, y, format2)
    size = font2.MeasureString(text, format2)
    y = y + size.Height + 6
    # Icon
    image = PdfImage.FromFile(inputFile1)
    page.Canvas.DrawImage(image, PointF(
        pageWidth - image.PhysicalDimension.Width, y))
    imageLeftSpace = pageWidth - image.PhysicalDimension.Width - 2
    imageBottom = image.PhysicalDimension.Height + y
    # Reference content
    font3 = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Regular, True)
    format3 = PdfStringFormat()
    format3.ParagraphIndent = font3.Size * 2
    format3.MeasureTrailingSpaces = True
    format3.LineSpacing = font3.Size * 1.5
    text1 = "(All text and picture from "
    text2 = "Wikipedia"
    text3 = ", the free encyclopedia)"
    page.Canvas.DrawString(text1, font3, brush2, 0.0, y, format3)
    size = font3.MeasureString(text1, format3)
    x1 = size.Width
    format3.ParagraphIndent = 0.0
    font4 = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Underline, True)
    brush3 = PdfBrushes.get_Blue()
    page.Canvas.DrawString(text2, font4, brush3, x1, y, format3)
    size = font4.MeasureString(text2, format3)
    x1 = x1 + size.Width
    page.Canvas.DrawString(text3, font3, brush2, x1, y, format3)
    y = y + size.Height
    # Content
    format4 = PdfStringFormat()
    text = ReadFromTxt(inputFile2)
    font5 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
    format4.LineSpacing = font5.Size * 1.5
    textLayouter = PdfStringLayouter()
    imageLeftBlockHeight = imageBottom - y
    result = textLayouter.Layout(text, font5, format4, SizeF(
        imageLeftSpace, imageLeftBlockHeight))
    if result.ActualSize.Height < imageBottom - y:
        imageLeftBlockHeight = imageLeftBlockHeight + result.LineHeight
        result = textLayouter.Layout(text, font5, format4, SizeF(
            imageLeftSpace, imageLeftBlockHeight))
    for line in result.Lines:
        page.Canvas.DrawString(line.Text, font5, brush2, 0.0, y, format4)
        y = y + result.LineHeight
    textWidget = PdfTextWidget(result.Remainder, font5, brush2)
    textLayout = PdfTextLayout()
    textLayout.Break = PdfLayoutBreakType.FitPage
    textLayout.Layout = PdfLayoutType.Paginate
    bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
    textWidget.StringFormat = format4
    newPage = PdfNewPage(page)
    textWidget.Draw(newPage, bounds, textLayout)


# Create a pdf document
doc = PdfDocument()
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
page.BackgroundColor = Color.get_Chocolate()
# Draw page
DrawPage(page)
page = doc.Pages.Add(PdfPageSize.A4(), margin)
page.BackgroundColor = Color.get_Coral()
# Draw page
DrawPage(page)
page = doc.Pages.Add(PdfPageSize.A3(
), margin, PdfPageRotateAngle.RotateAngle180, PdfPageOrientation.Landscape)
page.BackgroundColor = Color.get_LightPink()
# Draw page
DrawPage(page)
# create section
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
# Draw page
DrawPage(page)
# Set background color
page = section.Pages.Add()
page.BackgroundColor = Color.get_LightSkyBlue()
DrawPage(page)
# Landscape
section = doc.Sections.Add()
section.PageSettings.Orientation = PdfPageOrientation.Landscape
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
DrawPage(page)
# Rotate 90
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle90
DrawPage(page)
# Rotate 180
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle180
DrawPage(page)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
