from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToXLSX.xlsx"
inputFile = "./Demos/Data/ChartSample.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save the pdf file to excel
pdf.SaveToFile(outputFile, FileFormat.XLSX)
pdf.Close()
