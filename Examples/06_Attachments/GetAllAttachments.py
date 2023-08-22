from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_2.pdf"

#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get a collection of attachments on the PDF document.
collection = pdf.Attachments
#Save all the attachments to the files.
if collection.Count > 0:
    for i in range(collection.Count):
        attitem = collection.get_Item(i)
        attitem.Data.Save(attitem.FileName)
pdf.Close()


