
from spire.pdf.common import *
from spire.pdf import *
import math

inputfile = "./Demos/Data/ChartImage.png"
outputFile = "DrawImage.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()
#Save graphics state
state = page.Canvas.Save()
#Draw the text - transform           
font = PdfFont(PdfFontFamily.Helvetica, 18.0)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
brush2 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
strformat = PdfStringFormat(PdfTextAlignment.Center)
page.Canvas.TranslateTransform(math.trunc(page.Canvas.ClientSize.Width / float(2)), 20.0)
page.Canvas.DrawString("Chart image", font, brush1, 0.0, 0.0, strformat)
page.Canvas.ScaleTransform(1, -0.8)
page.Canvas.DrawString("Chart image", font, brush2, 0.0, -2 * 18 * 1.2, strformat)
# Restore graphics
page.Canvas.Restore(state)

#Load an image
image = PdfImage.FromFile(inputfile)
width = image.Width * 0.75
height = image.Height * 0.75
x = (page.Canvas.ClientSize.Width - width) / 2
#Draw the image
page.Canvas.DrawImage(image, x, 60.0, width, height)

skewX = 20.0
skewY = 20.0
scaleX = 0.2
scaleY = 0.6
width = float(((image.Width + image.Height * math.tan(math.pi * skewX/ 180)) * scaleX))
height = float(((image.Height + image.Width * math.tan(math.pi * skewY/ 180)) * scaleY))
template = PdfTemplate(width, height)
template.Graphics.ScaleTransform(scaleX, scaleY)
template.Graphics.SkewTransform(skewX, skewY)
template.Graphics.DrawImage(image, 0.0, 0.0)
#Save graphics state
state = page.Canvas.Save()
page.Canvas.TranslateTransform(page.Canvas.ClientSize.Width - 50, 260.0)
offset = math.trunc((page.Canvas.ClientSize.Width - 100) / float(12))
for i in range(0, 12):
    page.Canvas.TranslateTransform(-offset, 0.0)
    page.Canvas.SetTransparency(i / 12.0)
    page.Canvas.DrawTemplate(template, PointF(0.0, 0.0))
#Restore graphics
page.Canvas.Restore(state)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()
