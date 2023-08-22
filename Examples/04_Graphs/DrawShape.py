
from spire.pdf.common import *
from spire.pdf import *
import math

outputFile = "DrawShape.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()

#points = [PointF() for _ in range(5)]
points = [None]*5
i = 0
while i < 5:
    x = float(math.cos(i * 2 * math.pi / 5))
    y = float(math.sin(i * 2 * math.pi / 5))
    points[i] = PointF(x, y)
    i += 1
path = PdfPath()
path.AddLine(points[2], points[0])
path.AddLine(points[0], points[3])
path.AddLine(points[3], points[1])
path.AddLine(points[1], points[4])
path.AddLine(points[4], points[2])
#Save graphics state
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_DeepSkyBlue()), 0.02)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
page.Canvas.ScaleTransform(50.0, 50.0)
page.Canvas.TranslateTransform(5.0, 1.2)
page.Canvas.DrawPath(pen, path)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Alternate
page.Canvas.DrawPath(pen, brush1, path)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush1, path)
brush2 = PdfLinearGradientBrush(PointF(-2.0, 0.0), PointF(2.0, 0.0), PdfRGBColor(Color.get_Red()), PdfRGBColor(Color.get_Blue()))
page.Canvas.TranslateTransform(-4.0, 2.0)
path.FillMode = PdfFillMode.Alternate
page.Canvas.DrawPath(pen, brush2, path)
brush3 = PdfRadialGradientBrush(PointF(0.0, 0.0), 0.0, PointF(0.0, 0.0), 1.0, PdfRGBColor(Color.get_Red()) , PdfRGBColor(Color.get_Blue()))
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush3, path)
brush4 = PdfTilingBrush(RectangleF(0.0, 0.0, 4.0, 4.0))
brush4.Graphics.DrawRectangle(brush2, 0.0, 0.0, 4.0, 4.0)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush4, path)
# Restore graphics
page.Canvas.Restore(state)

#Save graphics state
state = page.Canvas.Save()
#Draw shape - Spiro
pen = PdfPens.get_DeepSkyBlue()
nPoints = 1000
r1 = 30
r2 = 25
p = 35
x1 = r1 + r2 - p
y1 = 0
x2 = 0
y2 = 0
page.Canvas.TranslateTransform(100.0, 100.0)
for i in range(0, nPoints):
    t = i * math.pi / 90
    x2 = (r1 + r2) * math.cos(t) - p * math.cos((r1 + r2) * t / r2)
    y2 = (r1 + r2) * math.sin(t) - p * math.sin((r1 + r2) * t / r2)
    page.Canvas.DrawLine(pen, float(x1), float(y1), float(x2), float(y2))
    x1 = x2
    y1 = y2
#Restore graphics
page.Canvas.Restore(state)

#Save graphics state
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_Chocolate()) , 1.0)
page.Canvas.DrawRectangle(pen, RectangleF(PointF(20.0, 310.0), SizeF(150.0, 120.0)))
#Restore graphics
page.Canvas.Restore(state)

#Save graphics state
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_DarkRed()), 2.0)
page.Canvas.DrawPie(pen, 220.0, 320.0, 100.0, 90.0, 360.0, 360.0)
#Restore graphics
page.Canvas.Restore(state)

#Save graphics state
state = page.Canvas.Save()
brush = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
page.Canvas.DrawEllipse(brush, 380.0, 325.0, 80.0, 80.0)
#Restore graphics
page.Canvas.Restore(state)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()
