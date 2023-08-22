from spire.pdf.common import *
from spire.pdf import *

def AppendText(fname: str, text: str):
    fp = open(fname, "w")
    fp.write(text + "\n")
    fp.close()

outputFile = "GetNumberOfPages.txt"
inputFile = "./Demos/Data/DeletePage.pdf"

# Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
count = doc.Pages.Count
AppendText(
    outputFile, "The page count of the pdf document is " + str(count))
doc.Close()
