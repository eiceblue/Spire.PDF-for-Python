
from spire.pdf.common import *
from spire.pdf import *
import math

inputfile = "./Demos/Data/DrawingTemplate.pdf"
outputFile = "SetRectangleTransparency_out.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw rectangles
x = 200.0
y = 300.0
width = 200.0
height = 100.0
pen = PdfPen(PdfRGBColor(Color.get_Black()), 1.0)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Red()))
page.Canvas.SetTransparency(0.5, 0.5)
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
x = x + math.trunc(width / float(2))
y = y - math.trunc(height / float(2))
page.Canvas.SetTransparency(0.2, 0.2)
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
#Restore graphics
page.Canvas.Restore(state)
#Save the document
pdf.SaveToFile(outputFile)
