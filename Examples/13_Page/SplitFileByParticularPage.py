from spire.pdf.common import *
from spire.pdf import *

outputFile = "SplitFileByParticularPage.pdf"
inputFile = "./Demos/Data/Sample.pdf"

#Create a pdf document
oldPdf = PdfDocument()
#Load an existing pdf from disk
oldPdf.LoadFromFile(inputFile)
#Create a new PDF document
newPdf = PdfDocument()
#Initialize a new instance of PdfPageBase class
page = None
#Specify the pages which you want them to be split
for i in range(1, 3):
    #Add same size page for newPdf
    page = newPdf.Pages.Add(oldPdf.Pages[i].Size, PdfMargins(0.0))
    #Create template of the oldPdf page and draw into newPdf page
    oldPdf.Pages[i].CreateTemplate().Draw(page, PointF(0.0, 0.0))
#Save the document
newPdf.SaveToFile(outputFile)
newPdf.Close()
