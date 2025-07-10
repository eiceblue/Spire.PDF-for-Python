from spire.pdf.common import *
from spire.pdf import *

outputFile = "CreateMultilayerPDF.pdf"
inputFile = "./Demos/Data/MultilayerImage.png"

doc = PdfDocument()
# Creates a page
page = doc.Pages.Add()
#Create text
text = "Welcome to evaluate Spire.PDF for Python !"
format = PdfStringFormat(PdfTextAlignment.Left)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
# Defines a font
font = PdfTrueTypeFont("Calibri", 15.0, PdfFontStyle.Regular,True)
x = 50.0
y = 50.0
# Draw text layer
page.Canvas.DrawString(text, font, brush, PointF(x, y), format)
size = font.MeasureString("Welcome to  evaluate", format)
size2 = font.MeasureString("Spire.PDF for Python", format)
# Loads an image 
image = PdfImage.FromFile(inputFile)
# Draw image layer
page.Canvas.DrawImage(image, PointF(x + size.Width, y),size2)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
