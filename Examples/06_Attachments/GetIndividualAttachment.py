from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_2.pdf"

#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get a collection of attachments on the PDF document.
collection = pdf.Attachments
#Get the second attachment in PDF file.
attachment = collection.get_Item(1)
#Save the second attachment to the file.
attachment.Data.Save(attachment.FileName)
pdf.Close()

