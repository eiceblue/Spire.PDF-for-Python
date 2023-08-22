from spire.pdf.common import *
from spire.pdf import *


outputFile =  "PdfAttachmentRelationship.pdf"
inputFile = "./Demos/Data/Attachment.pdf"
input_Img = "./Demos/Data/E-iceblueLogo.png"

#Create a pdf document
doc= PdfDocument()
doc.LoadFromFile(inputFile)
#Define PdfAttachment
attachment = PdfAttachment(input_Img)
#Add addachment
doc.Attachments.Add(attachment, doc, PdfAttachmentRelationship.Alternative)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

