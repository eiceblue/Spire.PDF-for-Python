from spire.pdf.common import *
from spire.pdf import *

outputFile = "SetTabOrder.pdf"
inputFile = "./Demos/Data/SetTabOrder.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Set using document structure
pdf.FileInfo.IncrementalUpdate = False
page = pdf.Pages[0]
page.SetTabOrder(TabOrder.Structure)
#Save the file
pdf.SaveToFile(outputFile)
pdf.Close()

