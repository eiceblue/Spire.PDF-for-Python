from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ReplaceTextInPage.pdf"
outputFile = "ReplaceTextInPage_out.pdf"
# Create a new PdfDocument
doc = PdfDocument()
# Load pdf file from disk
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Create a PdfTextReplacer using the first page
replacer = PdfTextReplacer(page)
# Replace all texts in this page
replacer.ReplaceAllText("Spire.PDF","E-iceblue")
# Replace the first found word
replacer.ReplaceText("Adobe Acrobat", "PDF editors")
doc.SaveToFile(outputFile)
doc.Close()