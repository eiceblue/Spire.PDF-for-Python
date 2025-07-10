from spire.pdf.common import *
from spire.pdf import *

inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "SearchTextAndAddHyperlink_out.pdf"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the matched phrases
finds =PdfTextFinder(page)
finds.Options.Parameter = TextFindParameter.IgnoreCase
collection = finds.Find("e-iceblue")

# hyperlink url
url = "http://www.e-iceblue.com"

for find in collection:
    # Create a PdfUriAnnotation object to add hyperlink for the searched text
    rec =RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)
    uri = PdfUriAnnotation(rec)
    uri.Uri = url
    uri.Border = PdfAnnotationBorder(1.0)
    uri.Color = PdfRGBColor(Color.get_Blue())
    page.AnnotationsWidget.Add(uri)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()


