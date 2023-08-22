from spire.pdf.common import *
from spire.pdf import *


outputFile = "RemoveHyperlinks.pdf"
inputFile = "./Demos/Data/RemoveHyperlinks.pdf"

# Load an existing PDF file
document = PdfDocument()
document.LoadFromFile(inputFile)
# Get the first page
page = document.Pages[0]
# Get the annotation collection
widgetCollection = page.AnnotationsWidget
# Verify whether widgetCollection is null or not
if widgetCollection.Count > 0:
    for i in range(widgetCollection.Count - 1, -1, -1):
        annotation = widgetCollection.get_Item(i)
        # Get the TextWebLink Annotation
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            link = annotation if isinstance(
                annotation, PdfTextWebLinkAnnotationWidget) else None
            # Remove the TextWebLink annotation
            widgetCollection.Remove(link)
document.SaveToFile(outputFile)
document.Close()
