from spire.pdf.common import *
from spire.pdf import *

outputFile = "RotateExistingPDF.pdf"
inputFile = "./Demos/Data/Sample.pdf"

# Create a pdf document
doc = PdfDocument()
# Load an existing pdf from disk
doc.LoadFromFile(inputFile)
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the original rotation angle
rotation = int(page.Rotation.value)
# Set the angle
rotation += int(PdfPageRotateAngle.RotateAngle270.value)
# Rotate the PDF page based on
page.Rotation = PdfPageRotateAngle(rotation)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
