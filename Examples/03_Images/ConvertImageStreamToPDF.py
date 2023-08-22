from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/bg.png"
outputFile = "ConvertImageStreamToPDF.pdf"

# Create a pdf document with a section and page added.
pdf = PdfDocument()
section = pdf.Sections.Add()
page = section.Pages.Add()
# Create a FileStream object to read the imag file
fileStream = Stream(inputFile1)
# Specify the image source as MemoryStream
image = PdfImage.FromStream(fileStream)
#Set image display location and size in PDF
#Calculate rate
widthFitRate = image.PhysicalDimension.Width / page.Canvas.ClientSize.Width
heightFitRate = image.PhysicalDimension.Height / page.Canvas.ClientSize.Height
fitRate = max(widthFitRate, heightFitRate)
#Calculate the size of image 
fitWidth = image.PhysicalDimension.Width / fitRate
fitHeight = image.PhysicalDimension.Height / fitRate
#Draw image
page.Canvas.DrawImage(image, 0.0, 30.0, fitWidth, fitHeight)
pdf.SaveToFile(outputFile)
pdf.Close()