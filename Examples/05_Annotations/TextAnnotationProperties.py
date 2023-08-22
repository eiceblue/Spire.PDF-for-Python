from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/FreeTextAnnotation.pdf"
outputFile = "CopyTextAnnotationProperties.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get the first page.
firstPage = pdf.Pages[0]
#Create a new PDF document.
newPdf = PdfDocument()
#Traverse the annotations of the first page of old PDF
annot = firstPage.AnnotationsWidget
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, PdfFreeTextAnnotationWidget):
            #Get its bounds and text
            rect = annotation.Bounds
            text = annotation.Text
            #Add new page for newPdf
            newPage = newPdf.Pages.Add(firstPage.Size)
            #Add annotation with the same settings as the annotation of old PDF
            newAnnotation = PdfFreeTextAnnotation(rect)
            newAnnotation.Text = text
            newAnnotation.CalloutLines = annotation.CalloutLines
            newAnnotation.LineEndingStyle = annotation.LineEndingStyle
            newAnnotation.AnnotationIntent=PdfAnnotationIntent.FreeTextCallout
            newAnnotation.RectangleDifferences = annotation.RectangularDifferenceArray
            newAnnotation.Color = annotation.Color
            newPage.AnnotationsWidget.Add(newAnnotation)
#Save the file
newPdf.SaveToFile(outputFile)
newPdf.Close()

