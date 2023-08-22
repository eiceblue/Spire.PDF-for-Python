from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToLinearizedPdf.pdf"
inputFile = "./Demos/Data/PDFTemplate_N.pdf"

converter = PdfToLinearizedPdfConverter(inputFile)
converter.ToLinearizedPdf(outputFile)
