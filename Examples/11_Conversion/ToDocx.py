from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToDocx.docx"
inputFile = "./Demos/Data/ToDocx.pdf"

# Load a pdf document
inputfile = inputFile
doc = PdfDocument()
doc.LoadFromFile(inputfile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.DOCX)
doc.Close()
