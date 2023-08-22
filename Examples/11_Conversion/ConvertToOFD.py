from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ConvertToOFD.ofd"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Convert pdf to ofd
doc.SaveToFile(outputFile, FileFormat.OFD)
doc.Close()
