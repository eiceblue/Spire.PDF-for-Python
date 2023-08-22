from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/PdfToExcel.pdf"
outputFile = "PdfToExcel.xlsx"

pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save the pdf file to excel
pdf.SaveToFile(outputFile, FileFormat.XLSX)
pdf.Close()
