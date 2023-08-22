from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/ChartImage.png"
outputFile = "Transparency.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one section
section = doc.Sections.Add()
#Load an image
image = PdfImage.FromFile(inputfile)
imageWidth = image.PhysicalDimension.Width / float(2)
imageHeight = image.PhysicalDimension.Height / float(2)
#for mode in Enum.GetValues(type_of(PdfBlendMode)):
for mode in PdfBlendMode.__members__:
    page = section.Pages.Add()
    pageWidth = page.Canvas.ClientSize.Width
    y = 0.0
    #Title
    y = y + 15
    brush = PdfSolidBrush(PdfRGBColor(Color.get_OrangeRed()))
    font = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold,True)
    format = PdfStringFormat(PdfTextAlignment.Center)
    text = "Transparency Blend Mode: {0:s}".format(mode)
    page.Canvas.DrawString(text, font, brush, pageWidth / 2, y, format)
    size = font.MeasureString(text, format)
    y = y + size.Height + 25
    page.Canvas.DrawImage(image, 0.0, y, imageWidth, imageHeight)
    page.Canvas.Save()
    d = (page.Canvas.ClientSize.Width - imageWidth) / 5
    x = d
    y = y + d / 2+40
    for i in range(0, 5):
        alpha = 1.0 / 6 * (5 - i)
        page.Canvas.SetTransparency(alpha, alpha, PdfBlendMode[mode])
        page.Canvas.DrawImage(image, x, y, imageWidth, imageHeight)
        x = x + d
        y = y + d / 2+ 40
    page.Canvas.Restore()
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
