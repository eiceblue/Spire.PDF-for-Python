
from spire.pdf.common import *
from spire.pdf import *

outputFile = "AddLayers.pdf.pdf"
inputFile = "./Demos/Data/AddLayers.pdf"

doc = PdfDocument()
doc.LoadFromFile(inputFile)
page = doc.Pages[0]
#create a layer named "red line"
layer = doc.Layers.AddLayer("red line",PdfVisibility.On)
pcA = layer.CreateGraphics(page.Canvas)
pcA.DrawLine(PdfPen(PdfBrushes.get_Red(), 2.0), PointF(100.0, 350.0), PointF(300.0, 350.0))
#create a layer named "blue line"
layer = doc.Layers.AddLayer("blue line")
pcB = layer.CreateGraphics(doc.Pages[0].Canvas)
pcB.DrawLine(PdfPen(PdfBrushes.get_Blue(), 2.0), PointF(100.0, 400.0), PointF(300.0, 400.0))
#create a layer named "green line"
layer = doc.Layers.AddLayer("green line")
pcC = layer.CreateGraphics(doc.Pages[0].Canvas)
pcC.DrawLine(PdfPen(PdfBrushes.get_Green(), 2.0), PointF(100.0, 450.0), PointF(300.0, 450.0))
#save the pdf document
doc.SaveToFile(outputFile)
doc.Close()
