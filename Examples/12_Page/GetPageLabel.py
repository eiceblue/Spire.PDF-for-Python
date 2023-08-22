from spire.pdf.common import *
from spire.pdf import *

def AppendAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s + "\n")
    fp.close()

outputFile = "GetPageLabel.txt"
inputFile = "./Demos/Data/PageLabel.pdf"

# Create a PdfDocument instance
pdf = PdfDocument()
# Load the PDF file
pdf.LoadFromFile(inputFile)
# Create a StringBuilder instance
sb = []
# Get the labels of the pages in the PDF file
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    sb.append("The page label of page "+str(i+1) +
              " is \""+page.PageLabel+"\"")
# Save them to a txt file
AppendAllText(outputFile, sb)
pdf.Close()