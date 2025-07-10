from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/LinkAnnotation.pdf"
outputFile = "LinkAnnotation.pdf"

#Create a pdf document
doc = PdfDocument()
#Load file from disk
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Get the annotation collection
widgetCollection = page.AnnotationsWidget
#Verify whether widgetCollection is null or not
if widgetCollection.Count > 0:
    for i in range(widgetCollection.Count):
        annotation = widgetCollection.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            #Get the link annotation
            link = annotation if isinstance(annotation, PdfTextWebLinkAnnotationWidget) else None
            #Change the url
            link.Url = "http://www.e-iceblue.com/Introduce/pdf-for-net-introduce.html"
#Save the document
doc.SaveToFile(outputFile)
doc.Close()