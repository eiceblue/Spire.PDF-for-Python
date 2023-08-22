from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DrawingTemplate.pdf"
outputFile = "DrawLine_out.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw line
#Set location and size
x = 95.0
y = 95.0
width = 400.0
height = 500.0
#Create pens
pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.1)
pen1 = PdfPen(PdfRGBColor(Color.get_Red()), 0.1)
#Draw a rectangle
page.Canvas.DrawRectangle(pen, x, y, width, height)
#Draw two crossed lines
page.Canvas.DrawLine(pen1, x, y, x + width, y + height)
page.Canvas.DrawLine(pen1, x + width, y, x, y + height)
#Restore graphics
page.Canvas.Restore(state)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()