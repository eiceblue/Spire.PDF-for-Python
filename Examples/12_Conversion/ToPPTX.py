from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Data/ToDocx.pdf"
outputFile = "ToPPTX.pptx"

pdf = PdfDocument()
pdf.LoadFromFile(inputFile)

# Save the pdf file to pptx
pdf.SaveToFile(outputFile, FileFormat.PPTX)
pdf.Close()
