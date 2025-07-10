from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_5.pdf"
outputFile = "IsPDFPortfolio.txt"

#Create a pdf document
doc = PdfDocument()
#Load from file
doc.LoadFromFile(inputFile)
builder = ""
#Judge whether the document is portfolio or not.
value = doc.IsPortfolio
if value:
    builder="The document is portfolio"
else:
    builder="The document is not portfolio"
#save
fp = open(outputFile,"w")
for s in builder:
    fp.write(s)
fp.close()
doc.Close()