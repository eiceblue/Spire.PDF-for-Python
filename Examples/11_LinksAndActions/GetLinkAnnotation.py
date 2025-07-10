from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/LinkAnnotation.pdf"
outputFile = "GetLinkAnnotation.txt"

#Create a pdf document
doc = PdfDocument()
#Load file from disk
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Get the annotation collection
annotations = page.AnnotationsWidget
#Create StringBuilder to save 
content = []
#Verify whether widgetCollection is not null or not
if annotations.Count > 0:
    #traverse the PdfAnnotationCollection
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #if it is PdfTextWebLinkAnnotationWidget
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            #Get the Url
            WebLinkAnnotation = annotation if isinstance(annotation, PdfTextWebLinkAnnotationWidget) else None
            url = WebLinkAnnotation.Url
            #Add strings to StringBuilder
            content.append("The url of link annotation is "+ url+"\r\n")
            content.append("The text of link annotation is " + WebLinkAnnotation.Text)
#Save them to a txt file
f2=open(outputFile,'w', encoding='UTF-8')
for item in content:
        f2.write(item)
f2.close()
doc.Close()

