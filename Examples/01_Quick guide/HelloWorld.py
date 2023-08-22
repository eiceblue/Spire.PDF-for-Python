from spire.pdf.common import *
from spire.pdf import *

outputFile = "HelloWorld.pdf"

#Create a pdf document
doc= PdfDocument()
#Create one page
page = doc.Pages.Add()
s = "Hello, World"
x = 10.0
y = 10.0
font = PdfFont(PdfFontFamily.Helvetica ,30.0)
color = PdfRGBColor(Color.get_Black())
textBrush = PdfSolidBrush(color)
#Draw the text
page.Canvas.DrawString(s, font, textBrush, x, y)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

