from spire.pdf.common import *
from spire.pdf import *

outputFile = "Booklet_out.pdf"
inputFile = "./Demos/Data/Booklet.pdf"

#Create a pdf document
doc = PdfDocument()
width = PdfPageSize.A4().Width * 2
height = PdfPageSize.A4().Height
doc.CreateBooklet(inputFile, width, height, True)
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()
