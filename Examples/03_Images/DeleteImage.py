
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Data/DeleteImage.pdf"
outputFile = "DeleteImage.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)

#Get the first page
page = pdf.Pages[0]

imageHelper = PdfImageHelper()

# Get a collection of images on one page
imageInfos = imageHelper.GetImagesInfo(page)

# Delete the first image
imageHelper.DeleteImage(imageInfos[0])

#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()