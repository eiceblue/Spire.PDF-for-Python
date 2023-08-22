from spire.pdf.common import *
from spire.pdf import *
import math

inputFile1 = "./Demos/Data/bg.png"
outputFile = "ConvertImageToPDF.pdf"

# Create a pdf document with a section and page added.
pdf = PdfDocument()
section = pdf.Sections.Add()
page = pdf.Pages.Add()
#Load a tiff image from system
image = PdfImage.FromFile(inputFile1)
#Set image display location and size in PDF
#Calculate rate
widthFitRate = math.trunc(image.PhysicalDimension.Width / float(page.Canvas.ClientSize.Width))
heightFitRate = math.trunc(image.PhysicalDimension.Height / float(page.Canvas.ClientSize.Height))
fitRate = max(widthFitRate, heightFitRate)
#Calculate the size of image 
fitWidth = image.PhysicalDimension.Width / fitRate
fitHeight = image.PhysicalDimension.Height / fitRate
#Draw image
page.Canvas.DrawImage(image, 0.0, 30.0, fitWidth, fitHeight)
pdf.SaveToFile(outputFile)
pdf.Close()