from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/GetZoomFactor.pdf"
outputFile = "GetZoomFactor.txt"

#Create a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
action = doc.AfterOpenAction
zoomvalue = action.Destination.Zoom
result = "The zoom factor of the document is "+ str(zoomvalue*100) +"%."
#save
fp = open(outputFile,"w")
fp.write(outputFile + "\n")
fp.close()