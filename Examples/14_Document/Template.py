from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/Header.png"
inputFile2 = "./Demos/Data/Footer.png"
inputFile3 = "./Demos/Data/Wikipedia_Science.png"
inputFile4 = "./Demos/Data/Summary_of_Science.txt"
outputFile = "Template.pdf"

def DrawPage( page):
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
    image = PdfImage.FromFile(inputFile3)
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
    format3.ParagraphIndent = 0
    font4 = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Underline, True)
    brush3 = PdfBrushes.get_Blue()
    page.Canvas.DrawString(text2, font4, brush3, x1, y, format3)
    size = font4.MeasureString(text2, format3)
    x1 = x1 + size.Width
    page.Canvas.DrawString(text3, font3, brush2, x1, y, format3)
    y = y + size.Height
    # Content
    format4 = PdfStringFormat()
    with open(inputFile4,'r') as f:
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

def SetDocumentTemplate( doc, pageSize, margin):
    leftSpace = PdfPageTemplateElement(margin.Left, pageSize.Height)
    doc.Template.Left = leftSpace
    topSpace = PdfPageTemplateElement(pageSize.Width, margin.Top)
    topSpace.Foreground = True
    doc.Template.Top = topSpace
    # Draw header label
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(PdfTextAlignment.Right)
    label = "Demo of Spire.Pdf"
    size = font.MeasureString(label, format)
    y = topSpace.Height - font.Height - 1
    pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.75)
    topSpace.Graphics.SetTransparency(0.5)
    topSpace.Graphics.DrawLine(
        pen, margin.Left, y, pageSize.Width - margin.Right, y)
    y = y - 1 - size.Height
    topSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_Black(), pageSize.Width - margin.Right, y, format)
    rightSpace = PdfPageTemplateElement(margin.Right, pageSize.Height)
    doc.Template.Right = rightSpace
    bottomSpace = PdfPageTemplateElement(pageSize.Width, margin.Bottom)
    bottomSpace.Foreground = True
    doc.Template.Bottom = bottomSpace
    # Draw footer label
    y = font.Height + 1
    bottomSpace.Graphics.SetTransparency(0.5)
    bottomSpace.Graphics.DrawLine(
        pen, margin.Left, y, pageSize.Width - margin.Right, y)
    y = y + 1
    pageNumber = PdfPageNumberField()
    pageCount = PdfPageCountField()
    pageNumberLabel = PdfCompositeField()
    pageNumberLabel.AutomaticFields = [pageNumber, pageCount]
    pageNumberLabel.Brush = PdfBrushes.get_Black()
    pageNumberLabel.Font = font
    pageNumberLabel.StringFormat = format
    pageNumberLabel.Text = "page {0} of {1}"
    pageNumberLabel.Draw(bottomSpace.Graphics,
                         pageSize.Width - margin.Right, y)
    headerImage = PdfImage.FromFile(inputFile1)
    pageLeftTop = PointF(-margin.Left, -margin.Top)
    header = PdfPageTemplateElement(
        pageLeftTop, headerImage.PhysicalDimension)
    header.Foreground = False
    header.Graphics.SetTransparency(0.5)
    header.Graphics.DrawImage(headerImage, 0.0, 0.0)
    doc.Template.Stamps.Add(header)
    footerImage = PdfImage.FromFile(inputFile2)
    y = pageSize.Height - footerImage.PhysicalDimension.Height
    footerLocation = PointF(-margin.Left, y)
    footer = PdfPageTemplateElement(
        footerLocation, footerImage.PhysicalDimension)
    footer.Foreground = False
    footer.Graphics.SetTransparency(0.5)
    footer.Graphics.DrawImage(footerImage, 0.0, 0.0)
    doc.Template.Stamps.Add(footer)

def SetSectionTemplate( section, pageSize, margin, label):
    leftSpace = PdfPageTemplateElement(margin.Left, pageSize.Height)
    leftSpace.Foreground = True
    section.Template.OddLeft = leftSpace
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(
        PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    y = (pageSize.Height - margin.Top - margin.Bottom) * (1 - 0.618)
    bounds = RectangleF(10.0, y, margin.Left - 20, font.Height + 6)
    leftSpace.Graphics.DrawRectangle(PdfBrushes.get_OrangeRed(), bounds)
    leftSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_White(), bounds, format)
    rightSpace = PdfPageTemplateElement(margin.Right, pageSize.Height)
    rightSpace.Foreground = True
    section.Template.EvenRight = rightSpace
    bounds = RectangleF(10.0, y, margin.Right - 20, font.Height + 6)
    rightSpace.Graphics.DrawRectangle(PdfBrushes.get_SaddleBrown(), bounds)
    rightSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_White(), bounds, format)

# Create a pdf document
doc = PdfDocument()
doc.ViewerPreferences.PageLayout = PdfPageLayout.TwoColumnLeft
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
SetDocumentTemplate(doc, PdfPageSize.A4(), margin)
# Create one section
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = PdfMargins(0.0)
SetSectionTemplate(section, PdfPageSize.A4(), margin, "Section 1")
# Create one page
page = section.Pages.Add()
# Draw page
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()