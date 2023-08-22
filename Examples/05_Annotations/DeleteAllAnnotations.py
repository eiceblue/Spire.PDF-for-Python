from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/Template_Pdf_3.pdf"
outputFile = "DeleteAllAnnotations.pdf"

#Create a new PDF document.
document = PdfDocument()
#Load the file from disk
document.LoadFromFile(inputfile)
#Remove all annotations
document.Pages[0].AnnotationsWidget.Clear()
#Save the document
document.SaveToFile(outputFile)
document.Close()