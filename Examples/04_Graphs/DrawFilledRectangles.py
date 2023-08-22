from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DrawingTemplate.pdf"
outputFile = "DrawFilledRectangles_out.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Create one page
page = pdf.Pages[0]
#save graphics state
state = page.Canvas.Save()
#Set rectangle display location and size
x = 200.0
y = 300.0
width = 200.0
height = 120.0
#Create one page and brush
pen = PdfPen(PdfRGBColor(Color.get_Black()), 1.0)
brush = PdfSolidBrush(PdfRGBColor(Color.get_OrangeRed()))
#Draw a filled rectangle
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
#restore graphics
page.Canvas.Restore(state)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()