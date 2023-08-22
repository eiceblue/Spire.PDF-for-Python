
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DrawingTemplate.pdf"
outputFile = "DrawDashedLine_out.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw line
#Set location and size
x = 150.0
y = 200.0
width = 300.0
#Create pens
pen = PdfPen(PdfRGBColor(Color.get_Red()), 3.0)
#Set dash style and pattern
pen.DashStyle = PdfDashStyle.Dash
pen.DashPattern = [1, 4, 1]
#Draw a rectangle
#Draw two crossed lines
page.Canvas.DrawLine(pen, x, y, x + width, y)
#Restore graphics
page.Canvas.Restore(state)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()