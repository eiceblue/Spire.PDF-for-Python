from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/ToImage.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToBMP-img-{0:d}.bmp".format(i)
    with pdf.SaveAsImage(i) as imageS:
        imageS.Save(fileName)
pdf.Close()