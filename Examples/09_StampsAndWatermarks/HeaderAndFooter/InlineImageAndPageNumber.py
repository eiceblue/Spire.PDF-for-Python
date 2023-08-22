from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/PDFTemplate_HF.pdf"
outputFile = "InlineImageAndPageNumber.pdf"

#Load Pdf from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
text1 = "Spire.Pdf is a robust component by"
text2 = "Technology Co., Ltd."
image = PdfImage.FromFile("./Demos/Data/Top-logo.png")
#Define font and bursh
font = PdfTrueTypeFont("Impact", 10.0, PdfFontStyle.Regular , True)
bursh = PdfBrushes.get_DarkGray()
#Get the size of text
s1 = font.MeasureString(text1)
s2 = font.MeasureString(text2)
x = 10.0
y = 10.0
#Define image size
imgSize = SizeF(image.Width / float(2), image.Height / float(2))
#Define rectangle and string format
size = SizeF(s1.Width, imgSize.Width)
rect1 = RectangleF(PointF(x, y), size)
format = PdfStringFormat(PdfTextAlignment.Left,PdfVerticalAlignment.Middle)
#Draw the text1
page.Canvas.DrawString(text1, font, bursh, rect1, format)
#Draw the image
x += s1.Width
page.Canvas.DrawImage(image, PointF(x, y), imgSize)
#Draw the text2
x += imgSize.Width
size = SizeF(s2.Width, imgSize.Height)
rect1 = RectangleF(PointF(x, y), size)
page.Canvas.DrawString(text2, font, bursh, rect1, format)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

