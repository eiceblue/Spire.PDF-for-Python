from spire.pdf.common import *
from spire.pdf import *

outputFile = "DeletePage.pdf"
inputFile = "./Demos/Data/DeletePage.pdf"

# Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Delete the fifth page
doc.Pages.RemoveAt(4)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
