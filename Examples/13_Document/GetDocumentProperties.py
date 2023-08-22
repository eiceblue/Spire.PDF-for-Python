from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "GetDocumentProperties.txt"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get document information
docInfo = doc.DocumentInformation
# Create a StringBuilder object to put the details
builder = []
builder.append("Author:"+docInfo.Author)
builder.append("Creation Date: "+ docInfo.CreationDate.ToString())
builder.append("Keywords: "+ docInfo.Keywords)
builder.append("Modify Date: "+ docInfo.ModificationDate.ToString())
builder.append("Subject: "+ docInfo.Subject)
builder.append("Title: "+ docInfo.Title)
fp = open(outputFile,"w")
for s in builder:
    fp.write(s + "\n")
fp.close()
