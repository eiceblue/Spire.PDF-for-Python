from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/OpenAction.pdf"
outputFile = "RemoveOpenAction.pdf"

#Create a pdf document
document = PdfDocument()
#Load an existing pdf from disk
document.LoadFromFile(inputFile)
#Remove action
document.AfterOpenAction = None
#Save the document
document.SaveToFile(outputFile)
document.Close()