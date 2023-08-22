from spire.pdf.common import *
from spire.pdf import *


def AppendAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s + "\n")
    fp.close()


outputFile = "output"
inputFile = "./Demos/Data/Extraction.pdf"

# create a pdf document.
doc = PdfDocument()
doc.LoadFromFile(inputFile)
sbuffer = []
images = []
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    sbuffer.append(page.ExtractText())
    for image in page.ExtractImages():
        images.append(image)
# save text
fileName = outputFile + "\Extraction.txt"
AppendAllText(fileName, sbuffer)
# save image
index = 0
for image in images:
    imageFileName = outputFile + "\Image-{0:d}.png".format(index)
    index += 1
    image.Save(imageFileName, ImageFormat.get_Png())
doc.Close()
