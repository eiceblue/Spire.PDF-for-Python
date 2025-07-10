from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "/Data/Template_Pdf_2.pdf"
inputFile2 = "/Data/Template_Pdf_5.pdf"
outputFile = "CompareDocument_result.pdf"

#Load the pdf document
doc1 = PdfDocument()
doc1.LoadFromFile(inputFile1)

doc2 = PdfDocument()
doc2.LoadFromFile(inputFile2)

# Create a PDF comparer object
compare = PdfComparer(doc1, doc2)

# Save the result of the comparison to a new PDF document
compare.Compare(outputFile)