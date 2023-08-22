from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_5.pdf"
outputFile = "InvisibleAllPdfLayers.pdf"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
for i in range(doc.Layers.Count):
    #Set all the Pdf layers invisible.
    doc.Layers.get_Item(i).Visibility = PdfVisibility.Off
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
