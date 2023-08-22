from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/DeleteImage.pdf"
outputFile = "DeleteImageSecondApproach.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
#Get the first page
page = pdf.Pages[0]
#Delete the first image on the page
page.DeleteImage(0)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()
