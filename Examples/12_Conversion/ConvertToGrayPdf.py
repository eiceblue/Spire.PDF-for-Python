from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ConvertToGrayPdf.pdf"

#Create a PdfGrayConverter with an pdf file
converter = PdfGrayConverter(inputFile)
#Convert the file to gray pdf
converter.ToGrayPdf(outputFile)