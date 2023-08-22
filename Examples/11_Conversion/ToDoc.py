from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToDoc.doc"
inputFile = "./Demos/Data/ToDoc.pdf"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.DOC)
doc.Close()
