from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
outputFile= "AddBorderForText-result.pdf"

#Create a pdf document
doc = PdfDocument()
#Load from file
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
text = "Hello, World2!"
font = PdfTrueTypeFont("Times New Roman", 11.0, PdfFontStyle.Regular,True)
size = font.MeasureString(text)
color = PdfRGBColor(Color.get_Black())
brush = PdfSolidBrush(color)
x = 60.0
y = 600.0
#Draw the text on page
page.Canvas.DrawString(text, font, brush, x, y)
#Draw border for text  
page.Canvas.DrawRectangle(PdfPen(brush, 0.5),RectangleF(x, y, size.Width, size.Height))
#save to file
doc.SaveToFile(outputFile)
doc.Close()
