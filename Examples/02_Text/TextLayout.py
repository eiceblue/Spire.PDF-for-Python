from spire.pdf.common import *
from spire.pdf import *

def ReadText(fname:str):
    with open(fname, 'r') as f:
      content = f.read()
      return content


inputFile1 = "./Data/Wikipedia_Science.png"
inputFile2 = "./Data/Summary_of_Science.txt"
outputFile = "TextLayout.pdf"

  #Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()
pageWidth = page.Canvas.ClientSize.Width
y = 0.0

#Page header
pen1 = PdfPen(PdfRGBColor(Color.get_LightGray()) , 1.0)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_LightGray()))
font1 = PdfTrueTypeFont("Arial", 8.0, PdfFontStyle.Italic,True)
format1 = PdfStringFormat(PdfTextAlignment.Right)
text = "Demo of Spire.Pdf"
page.Canvas.DrawString(text, font1, brush1, pageWidth - 2, y, format1)
size = font1.MeasureString(text, format1)
y = y + size.Height + 1
page.Canvas.DrawLine(pen1, 0.0, y, pageWidth, y)

#Title
y = y + 25
brush2 = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
font2 = PdfTrueTypeFont("Arial", 18.0, PdfFontStyle.Bold,True)
format2 = PdfStringFormat(PdfTextAlignment.Center)
format2.CharacterSpacing = 1
text = "Summary of Science"
page.Canvas.DrawString(text, font2, brush2, pageWidth / 2, y, format2)
size = font2.MeasureString(text, format2)
y = y + size.Height + 16

#Icon
image = PdfImage.FromFile(inputFile1)
page.Canvas.DrawImage(image, PointF(pageWidth - image.PhysicalDimension.Width, y))
imageLeftSpace = pageWidth - image.PhysicalDimension.Width - 2
imageBottom = image.PhysicalDimension.Height + y

#Refenrence content
font3 = PdfTrueTypeFont("Arial", 12.0,PdfFontStyle.Regular,True)
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
font4 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Underline,True)
brush3 = PdfBrushes.get_Blue()
page.Canvas.DrawString(text2, font4, brush3, x1, y, format3)
size = font4.MeasureString(text2, format3)
x1 = x1 + size.Width

page.Canvas.DrawString(text3, font3, brush2, x1, y, format3)
y = y + size.Height

#Content
format4 = PdfStringFormat()
text = ReadText(inputFile2)
font5 = PdfTrueTypeFont("Arial", 12.0,PdfFontStyle.Regular,True)
format4.LineSpacing = font5.Size * 1.5
textLayouter = PdfStringLayouter()
imageLeftBlockHeight = imageBottom - y
result = textLayouter.Layout(text, font5, format4, SizeF(imageLeftSpace, imageLeftBlockHeight))
if result.ActualSize.Height < imageBottom - y:
    imageLeftBlockHeight = imageLeftBlockHeight + result.LineHeight
    result = textLayouter.Layout(text, font5, format4, SizeF(imageLeftSpace, imageLeftBlockHeight))
for line in result.Lines:
    page.Canvas.DrawString(line.Text, font5, brush2, 0.0, y, format4)
    y = y + result.LineHeight+2
textWidget = PdfTextWidget(result.Remainder, font5, brush2)
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
textWidget.StringFormat = format4
textWidget.Draw(page, bounds, textLayout)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()