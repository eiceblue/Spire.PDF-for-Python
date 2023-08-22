from spire.pdf.common import *
from spire.pdf import *

inputFile  =  "./Demos/Data/DeleteLayer.pdf"
outputFile = "DeleteLayer.pdf"

#Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Delete the "red line" layer
doc.Layers.RemoveLayer("red line")
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

