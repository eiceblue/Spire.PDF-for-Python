from spire.pdf.common import *
from spire.pdf import *

outputFile = "InsertEmptyPageAtEnd.pdf"
inputFile = "./Demos/Data/MultipagePDF.pdf"

# Load Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Add an empty page at the end
doc.Pages.Add(PdfPageSize.A4(), PdfMargins(0.0, 0.0))
# Save the Pdf document
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
