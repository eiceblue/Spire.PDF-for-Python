from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "ExtractTextFromParticularPage_out.txt"


doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page
page = doc.Pages[0]
# Extract text from page keeping white space
text = page.ExtractText(True)
# Write a line of text to the file
WriteAllText(outputFile, text)
doc.Close()