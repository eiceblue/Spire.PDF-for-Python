from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ImageWaterMark.pdf"
inputFile_img = "./Demos/Data/Background.png"
outputFile = "ImageWaterMark.pdf"

#Create a pdf document and load file from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Load image
img = Stream(inputFile_img)
#Set background image
page.BackgroundImage = img
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()