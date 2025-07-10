from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "SpecifyPageToView.pdf"

#Create a pdf document
doc = PdfDocument()
#Load file from disk.
doc.LoadFromFile(inputFile)
#Create a PdfDestination with specific page, location and 50% zoom factor
dest = PdfDestination(2, PointF(0.0, 100.0), 0.5)
#Create GoToAction with dest
action = PdfGoToAction(dest)
#Set open action
doc.AfterOpenAction = action
#Save the document
doc.SaveToFile(outputFile)
doc.Close()