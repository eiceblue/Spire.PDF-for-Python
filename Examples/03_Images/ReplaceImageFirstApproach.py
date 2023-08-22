from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/ReplaceImage.pdf"
inputImg = "./Demos/Data/E-iceblueLogo.png"
outputFile = "ReplaceImageFirstApproach.pdf"

#Create a pdf document
doc = PdfDocument()
#Load file from disk.
doc.LoadFromFile(inputfile)
#Get the first page.
page = doc.Pages[0]
#Get images of the first page.
imageInfo = page.ImagesInfo
#Replace the first image on the page.
page.ReplaceImage(0, PdfImage.FromFile( inputImg))
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
