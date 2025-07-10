from spire.pdf.common import *
from spire.pdf import *

outputFile = "output"
inputFile = "./Demos/Data/ToImage.pdf"

# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Save to images
for i in range(doc.Pages.Count):
    fileName = outputFile + "\\ToImage-img-{0:d}.png".format(i)
    with doc.SaveAsImage(i) as imageS:
        imageS.Save(fileName)
doc.Close()
