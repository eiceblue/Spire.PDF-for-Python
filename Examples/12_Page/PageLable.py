from spire.pdf.common import *
from spire.pdf import *

outputFile = "PageLable_1.pdf"
inputFile = "./Demos/Data/Sample.pdf"

# Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
doc.PageLabels = PdfPageLabels()
doc.PageLabels.AddRange(
    0, PdfPageLabels.Decimal_Arabic_Numerals_Style(), "label test")
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
