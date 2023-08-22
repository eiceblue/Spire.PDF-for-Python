from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToPostScript.ps"
inputFile = "./Demos/Data/ToPostScript.pdf"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to PostScript file.
doc.SaveToFile(outputFile, FileFormat.POSTSCRIPT)
doc.Close()
