from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/UpdateFreeTextAnnotation.pdf"
outputFile = "UpdateFreeTextAnnotation.pdf"

#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get the annotation Collection from the document.
annotations = pdf.Pages[0].AnnotationsWidget
#Update free text annotation.
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        annotation.Color = PdfRGBColor(Color.get_YellowGreen())
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()
