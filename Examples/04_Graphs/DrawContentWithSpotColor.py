
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DrawContentWithSpotColor.pdf"
outputFile = "SpotColor.pdf"

#Load the document from disk
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Get the first page
page = pdf.Pages[0]
#Initialize an instance of PdfSeparationColorSpace
cs = PdfSeparationColorSpace("MySpotColor", PdfRGBColor(Color.get_DarkViolet()))
#Set tini = 1 for the cs
color = PdfSeparationColor(cs, 1.0)
#Create a brush with spot color
brush = PdfSolidBrush(color)
#Draw a string
page.Canvas.DrawString("Tint=1.0", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(160.0, 160.0))
#Draw pie with spot color(DarkViolet)
page.Canvas.DrawPie(brush, 148.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.7", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(230.0, 160.0))
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.4", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(300.0, 160.0))
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.1", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(370.0, 160.0))
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 200.0, 60.0, 60.0, 360.0, 360.0)
#Draw pie with spot color(Purple)
cs = PdfSeparationColorSpace("MySpotColor",PdfRGBColor(Color.get_Purple()))
color = PdfSeparationColor(cs, 1.0)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 148.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 280.0, 60.0, 60.0, 360.0, 360.0)
#Draw pie with spot color(DarkSlateBlue)
cs = PdfSeparationColorSpace("MySpotColor",PdfRGBColor(Color.get_DarkSlateBlue()))
color = PdfSeparationColor(cs, 1.0)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 148.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 360.0, 60.0, 60.0, 360.0, 360.0)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()