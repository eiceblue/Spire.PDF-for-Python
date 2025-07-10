from spire.pdf.common import *
from spire.pdf import *

outputFile = "SvgToPdf.pdf"
inputFile = "./Demos/Data/template.svg"

# Create a new PDF document.
doc = PdfDocument()
# Load the file from disk.
doc.LoadFromSvg(inputFile)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
