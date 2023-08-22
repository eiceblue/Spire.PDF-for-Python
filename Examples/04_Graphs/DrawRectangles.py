from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DrawingTemplate.pdf"
outputFile = "DrawRectangles_out.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw rectangles
#Set rectangle display location and size
x = 130.0
y = 100.0
width = 400.0
height = 400.0
#Create one page
pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.1)
page.Canvas.DrawRectangle(pen, RectangleF(PointF(x, y), SizeF(width, height)))
y = y + height - 50
width = 100.0
height = 50.0
#Initialize an instance of PdfSeparationColorSpace
cs = PdfSeparationColorSpace("MyColor", PdfRGBColor(Color.FromArgb(0, 100, 0, 0)))
pen1 = PdfPen(PdfRGBColor(Color.get_Red()), 1.0)
#Create a brush with spot color
brush = PdfSolidBrush(PdfSeparationColor(cs, 0.1))
page.Canvas.DrawRectangle(pen1, brush, RectangleF(PointF(x, y), SizeF(width, height)))
#add by eric
page.Canvas.DrawLine(pen, 130.0, 200.0,400.0,400.0)
page.Canvas.DrawLine(pen, 130.0, 100.0, 530.0, 500.0)
#Restore graphics
page.Canvas.Restore(state)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()