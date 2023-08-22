from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToXPS.xps"
inputFile = "./Demos/Data/ToXPS.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save the pdf file to xps
pdf.SaveToFile(outputFile, FileFormat.XPS)
pdf.Close()