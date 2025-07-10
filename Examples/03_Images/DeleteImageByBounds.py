
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DeleteImageByBounds.pdf"
outputFile = "DeleteImageByBounds.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Get the first page
page = pdf.Pages[0]
#change:imageInfo = page.ImagesInfo
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
for i in range(len(imageInfo)):
    if imageInfo[i].Bounds.Contains(49.68, 73.1):
        imageHelper.DeleteImage(imageInfo[i])# change: page.DeleteImage(page.ImagesInfo[i])
    if imageInfo[i].Bounds.IntersectsWith(RectangleF(100.0, 500.0, 30.0, 40.0)):
        imageHelper.DeleteImage(imageInfo[i])# change: page.DeleteImage(page.ImagesInfo[i])
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()