from spire.pdf.common import *
from spire.pdf import *

outputFile = "InsertEmptyPage.pdf"
inputFile = "./Demos/Data/Sample.pdf"

# Create a pdf document
doc = PdfDocument()
# Load an existing pdf from disk
doc.LoadFromFile(inputFile)
# insert a blank page as the second page
doc.Pages.Insert(1)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
