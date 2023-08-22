from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ToImage.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToEMF-img-{0:d}.emf".format(i)
    with pdf.SaveAsImage(i,PdfImageType.Bitmap) as imageS:
         imageS.Save(fileName)
pdf.Close()