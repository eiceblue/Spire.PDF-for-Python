from spire.pdf.common import *
from spire.pdf import *

outputFile = "ChangePdfVersion.pdf"
inputFile = "./Demos/Data/ChangePdfVersion.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Change the pdf version
doc.FileInfo.Version = PdfVersion.Version1_6
doc.SaveToFile(outputFile)
doc.Close()
