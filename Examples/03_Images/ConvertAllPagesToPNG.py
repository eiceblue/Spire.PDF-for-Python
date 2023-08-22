from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/ToImage.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToPNG-img-{0:d}.png".format(i)
    with pdf.SaveAsImage(i) as imageS:
         imageS.Save(fileName)
pdf.Close()
