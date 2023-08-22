from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SetZoomFactor.pdf"
outputFile = "SetZoomFactor.pdf"

#Open a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Set pdf destination
dest = PdfDestination(page)
dest.Mode = PdfDestinationMode.Location
dest.Location = PointF(-40.0, -40.0)
dest.Zoom = 0.6
#Set action
gotoAction = PdfGoToAction(dest)
doc.AfterOpenAction = gotoAction
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()
