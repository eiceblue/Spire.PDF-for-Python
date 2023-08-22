from spire.pdf.common import *
from spire.pdf import *


inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "SearchTextAndDrawRectangle_out.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Create PdfTextFindCollection object to find all the matched phrases
collection = page.FindText("Spire.PDF for Python", TextFindParameter.IgnoreCase)
for find in collection.Finds:
    # Draw a rectangle with red pen
    page.Canvas.DrawRectangle(PdfPen(PdfBrushes.get_Red() ,0.9), find.Bounds)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()