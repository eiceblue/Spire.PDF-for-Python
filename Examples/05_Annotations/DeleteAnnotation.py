from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/DeleteAnnotation.pdf"
outputFile = "DeleteAnnotation.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Remove the first annotation
doc.Pages[0].AnnotationsWidget.RemoveAt(0)
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()
