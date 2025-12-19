from spire.pdf.common import *
from spire.pdf import *

inputFile = "Data/Template_Pdf_2.pdf"
outputFile = "GetPdfAttachmentInfo.txt"

#Create a new PDF document
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get a collection of attachments on the PDF document
collection = pdf.Attachments
#Get the first attachment.
attachment = collection.get_Item(0)
#Get the information of the first attachment.
content = []
content.append("Filename: " + attachment.FileName)
content.append("Description: " + attachment.Description)
content.append("Creation Date: " + attachment.CreationDate.strftime("%Y/%m/%d %H:%M:%S"))
content.append("Modification Date: " + attachment.ModificationDate.strftime("%Y/%m/%d %H:%M:%S"))
#Save to file.
with open(outputFile, "w") as file:
    file.write("\n".join(content))
pdf.Close()