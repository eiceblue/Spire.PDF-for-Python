from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToSVG.svg"
inputFile = "./Demos/Data/ToSVG.pdf"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to SVG file.
doc.SaveToFile(outputFile, FileFormat.SVG)
doc.Close()
