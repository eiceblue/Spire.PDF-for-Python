from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/TextStamp.pdf"
outputFile = "SetPropertiesForStamp.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get the first page
page = pdf.Pages[0]
#Traverse annotations widget
annot = page.AnnotationsWidget
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        #If it is PdfRubberStampAnnotationWidget
        if isinstance(annotation, PdfRubberStampAnnotationWidget):
            stamp = annotation if isinstance(annotation, PdfRubberStampAnnotationWidget) else None
            stamp.Author = "TestUser"
            stamp.Subject = "E-iceblue"
            stamp.CreationDate = DateTime.get_Now()
            stamp.ModifiedDate = DateTime.get_Now()
#Save to a pdf file
pdf.SaveToFile(outputFile, FileFormat.PDF)
pdf.Close()