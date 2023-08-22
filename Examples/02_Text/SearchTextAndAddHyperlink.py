from spire.pdf.common import *
from spire.pdf import *

inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "SearchTextAndAddHyperlink_out.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Create PdfTextFindCollection object to find all the matched phrases
collection = page.FindText("e-iceblue", TextFindParameter.IgnoreCase)
# hyperlink url
url = "http://www.e-iceblue.com"
for find in collection.Finds:
    # Create a PdfUriAnnotation object to add hyperlink for the searched text 
    uri = PdfUriAnnotation(find.Bounds)
    uri.Uri = url
    uri.Border = PdfAnnotationBorder(1.0)
    uri.Color = PdfRGBColor(Color.get_Blue())
    page.AnnotationsWidget.Add(uri)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
