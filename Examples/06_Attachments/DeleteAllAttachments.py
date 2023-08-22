from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/DeleteAllAttachments.pdf"
outputFile = "DeleteAllAttachments.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get all attachments
attachments = doc.Attachments
#Delete all attachments
attachments.Clear()
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()

