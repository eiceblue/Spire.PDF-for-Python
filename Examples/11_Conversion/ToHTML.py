from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToHTML.html"
inputFile = "./Demos/Data/ToHTML.pdf"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.HTML)
doc.Close()
