from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/ChartImage.png"
outputFile = "SetImageSize_out.pdf"

# Create a pdf document.
doc = PdfDocument()

# Create one page
page = doc.Pages.Add()

# Load an image
image = PdfImage.FromFile(inputfile)

# Set the width and height of image
width = image.Width * 0.75
height = image.Height * 0.75

# Define a position to draw image
x = (page.Canvas.ClientSize.Width - width) / 2
y = 60.0

# Draw image on page canvas
page.Canvas.DrawImage(image, x, y, width, height)

# Save the document
doc.SaveToFile(outputFile)
doc.Dispose()

