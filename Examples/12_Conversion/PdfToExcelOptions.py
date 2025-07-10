from spire.pdf.common import *
from spire.pdf import *


outputFile = "PdfToExcelOptions.xlsx"
inputFile = "./Demos/Data/PdfToXlsxOptions.pdf"

pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
pdf.ConvertOptions.SetPdfToXlsxOptions(
    XlsxLineLayoutOptions(False, True, True))
# Save the pdf file to excel
pdf.SaveToFile(outputFile, FileFormat.XLSX)
pdf.Close()
