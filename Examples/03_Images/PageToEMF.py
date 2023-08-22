from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/PageToImage.pdf"
outputFile = "PageToEMF.emf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Save to images
with pdf.SaveAsImage(1) as imageS:
    imageS.Save(outputFile)
pdf.Close()

