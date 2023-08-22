from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/Wikipedia_Science.png"
inputFile2 = "./Demos/Data/Summary_of_Science.txt"
outputFile = "Transition.pdf"

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
    font3 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
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
    with open(inputFile2,'r') as f:
        text = f.read()
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
doc.ViewerPreferences.PageMode = PdfPageMode.FullScreen
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create one section
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
# section.PageSettings.Transition = PdfPageTransition()
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Fly
section.PageSettings.Transition.PageDuration = 1.0
page = section.Pages.Add()
page.BackgroundColor = Color.get_Red()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Green()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Blue()
DrawPage(page)
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
# section.PageSettings.Transition = PdfPageTransition()
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Box
section.PageSettings.Transition.PageDuration = 1.0
page = section.Pages.Add()
page.BackgroundColor = Color.get_Orange()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Brown()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Navy()
DrawPage(page)
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
# section.PageSettings.Transition = PdfPageTransition()
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Split
section.PageSettings.Transition.Dimension = PdfTransitionDimension.Vertical
section.PageSettings.Transition.Motion = PdfTransitionMotion.Inward
section.PageSettings.Transition.PageDuration = 1.0
page = section.Pages.Add()
page.BackgroundColor = Color.get_Orange()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Brown()
DrawPage(page)
page = section.Pages.Add()
page.BackgroundColor = Color.get_Navy()
DrawPage(page)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
