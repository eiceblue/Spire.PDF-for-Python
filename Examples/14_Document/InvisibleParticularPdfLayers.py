from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_5.pdf"
outputFile = "InvisibleParticularPdfLayers.pdf"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Set the first layer invisible.
doc.Layers.get_Item(0).Visibility = PdfVisibility.Off
#Set the layer named "blue line" invisible.
doc.Layers.get_Item("blue line").Visibility = PdfVisibility.Off
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
