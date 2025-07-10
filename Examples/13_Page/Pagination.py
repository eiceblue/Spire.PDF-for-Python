from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/SciencePersonificationBoston.jpg"
inputFile2 = "./Demos/Data/Summary_of_Science.txt"
inputFile3 = "./Demos/Data/Header.png"
inputFile4 = "./Demos/Data/Footer.png"
outputFile = "Pagination.pdf"

def ReadFromTxt(fname: str) -> str:
    with open(fname, 'r') as f:
        text = f.read()
    return text

def DrawCover(section, margin):
    section.PageSettings.Size = PdfPageSize.A4()
    section.PageSettings.Margins.All = 0.0
    page = section.Pages.Add()
    DrawPageHeaderAndFooter(page, margin, True)
    # Reference content
    brush1 = PdfBrushes.get_LightGray()
    brush2 = PdfBrushes.get_Blue()
    font1 = PdfTrueTypeFont("Arial", 8.0, PdfFontStyle.Regular, True)
    format = PdfStringFormat()
    format.MeasureTrailingSpaces = True
    text1 = "(All text and picture from "
    text2 = "Wikipedia"
    text3 = ", the free encyclopedia)"
    x = 0.0
    y = 10.0
    x = x + margin.Left
    y = y + margin.Top
    page.Canvas.DrawString(text1, font1, brush1, x, y, format)
    x = x + font1.MeasureString(text1, format).Width
    page.Canvas.DrawString(text2, font1, brush2, x, y, format)
    x = x + font1.MeasureString(text2, format).Width
    page.Canvas.DrawString(text3, font1, brush1, x, y, format)
    # Cover
    brush3 = PdfBrushes.get_Black()
    brush4 = PdfSolidBrush(PdfRGBColor(0xf9, 0xf9, 0xf9))
    image = PdfImage.FromFile(inputFile1)
    text = "Personification of \"Science\" in front of the Boston Public Library"
    r = image.PhysicalDimension.Height / float(image.Height)
    pen = PdfPen(brush1, r)
    size = font1.MeasureString(text, image.PhysicalDimension.Width - 2)
    template = PdfTemplate(image.PhysicalDimension.Width + 4 * r + 4,
                           image.PhysicalDimension.Height + 4 * r + 7 + size.Height)
    template.Graphics.DrawRectangle(
        pen, brush4, 0.0, 0.0, template.Width, template.Height)
    x = y = r + 2
    template.Graphics.DrawRectangle(
        brush1, x, y, image.PhysicalDimension.Width + 2 * r, image.PhysicalDimension.Height + 2 * r)
    x = y = x + r
    template.Graphics.DrawImage(image, x, y)
    x = x - 1
    y = y + image.PhysicalDimension.Height + r + 2
    template.Graphics.DrawString(
        text, font1, brush3, RectangleF(PointF(x, y), size))
    x1 = (page.Canvas.ClientSize.Width - template.Width) / float(2)
    y1 = (page.Canvas.ClientSize.Height - margin.Top - margin.Bottom) * \
        (1 - 0.618) - template.Height / float(2) + margin.Top
    grWidget = PdfGraphicsWidget(template)
    grWidget.Draw(page.Canvas, x1, y1)
    # Title
    format.Alignment = PdfTextAlignment.Center
    font2 = PdfTrueTypeFont("Arial", 24.0, PdfFontStyle.Bold, True)
    x = page.Canvas.ClientSize.Width / float(2)
    y = y1 + template.Height + 10
    page.Canvas.DrawString("Science History and Etymology",
                           font2, brush3, x, y, format)

def DrawContent(section, margin):
    section.PageSettings.Size = PdfPageSize.A4()
    section.PageSettings.Margins.All = 0.0
    page = section.Pages.Add()
    DrawPageHeaderAndFooter(page, margin, False)
    x = margin.Left
    y = margin.Top + 8
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Regular,  True)
    brush1 = PdfBrushes.get_Black()
    pen1 = PdfPen(brush1, 0.75)
    page.Canvas.DrawString(
        "Science History and Etymology", font1, brush1, x, y)
    y = y + font1.MeasureString("Science History and Etymology").Height + 6
    page.Canvas.DrawLine(
        pen1, x, y, page.Canvas.ClientSize.Width - margin.Right, y)
    y = y + 1.75
    content = ReadFromTxt(inputFile2)
    lines = content.split('\n')
    font2 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Italic, True)
    format1 = PdfStringFormat()
    format1.MeasureTrailingSpaces = True
    format1.LineSpacing = font2.Height * 1.5
    format1.ParagraphIndent = font2.MeasureString("\t", format1).Width
    y = y + font2.Height * 0.5
    size = font2.MeasureString(lines[0], width, format1)
    page.Canvas.DrawString(lines[0], font2, brush1,
                           RectangleF(PointF(x, y), size), format1)
    y = y + size.Height
    font3 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
    format2 = PdfStringFormat()
    format2.LineSpacing = font3.Height * 1.4
    format2.MeasureTrailingSpaces = True
    size = font3.MeasureString(lines[1], width, format2)
    page.Canvas.DrawString(lines[1], font3, brush1,
                           RectangleF(PointF(x, y), size), format2)
    y = y + size.Height
    y = y + font3.Height * 0.75
    indent = font3.MeasureString("\t\t", format2).Width
    x1 = x + indent
    size = font3.MeasureString(lines[2], width - indent, format2)
    page.Canvas.DrawString(lines[2], font3, brush1,
                           RectangleF(PointF(x1, y), size), format2)
    y = y + size.Height + font3.Height * 0.75
    buff = []
    i = 3
    while i < len(lines):
        buff.append(lines[i])
        i += 1
    content = str(buff)
    textLayouter = PdfStringLayouter()
    result = textLayouter.Layout(
        content, font3, format2, SizeF(width, 999999.0))
    for line in result.Lines:
        if (line.intLineType & LineType.FirstParagraphLine.value == LineType.FirstParagraphLine.value):
            y = y + font3.Height * 0.75
        if y > (page.Canvas.ClientSize.Height - margin.Bottom - result.LineHeight):
            page = section.Pages.Add()
            DrawPageHeaderAndFooter(page, margin, False)
            y = margin.Top
        page.Canvas.DrawString(line.Text, font3, brush1, x, y, format2)
        y = y + result.LineHeight

def DrawPageHeaderAndFooter(page, margin, isCover):
    page.Canvas.SetTransparency(0.5)
    headerImage = PdfImage.FromFile(inputFile3)
    footerImage = PdfImage.FromFile(inputFile4)
    page.Canvas.DrawImage(headerImage, PointF(0.0, 0.0))
    page.Canvas.DrawImage(footerImage, PointF(
        0.0, page.Canvas.ClientSize.Height - footerImage.PhysicalDimension.Height))
    if isCover:
        page.Canvas.SetTransparency(1.0)
        return
    brush = PdfBrushes.get_Black()
    pen = PdfPen(brush, 0.75)
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(PdfTextAlignment.Right)
    format.MeasureTrailingSpaces = True
    space = font.Height * 0.75
    x = margin.Left
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    y = margin.Top - space
    page.Canvas.DrawLine(pen, x, y, x + width, y)
    y = y - 1 - font.Height
    page.Canvas.DrawString("Demo of Spire.Pdf", font,
                           brush, x + width, y, format)
    page.Canvas.SetTransparency(1.0)

def DrawPageNumber(section, margin, startNumber, pageCount):
    for i in range(section.Pages.Count):
        page = section.Pages.get_Item(i)
        page.Canvas.SetTransparency(0.5)
        brush = PdfBrushes.get_Black()
        pen = PdfPen(brush, 0.75)
        font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
        format = PdfStringFormat(PdfTextAlignment.Right)
        format.MeasureTrailingSpaces = True
        space = font.Height * 0.75
        x = margin.Left
        width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
        y = page.Canvas.ClientSize.Height - margin.Bottom + space
        page.Canvas.DrawLine(pen, x, y, x + width, y)
        y = y + 1
        numberLabel = "{0:d} of {1:d}".format(startNumber, pageCount)
        startNumber += 1
        page.Canvas.DrawString(numberLabel, font, brush, x + width, y, format)
        page.Canvas.SetTransparency(1.0)


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
DrawCover(doc.Sections.Add(), margin)
DrawContent(doc.Sections.Add(), margin)
DrawPageNumber(doc.Sections.get_Item(1), margin,
               1, doc.Sections.get_Item(1).Pages.Count)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
