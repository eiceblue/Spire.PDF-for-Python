from spire.pdf.common import *
from spire.pdf import *


inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "SearchTextAndDrawRectangle_out.pdf"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the matched phrases
finds =PdfTextFinder(page)
finds.Options.Parameter =TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")

for find in collection:
    # Draw a rectangle with red pen
    rec =RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)
    page.Canvas.DrawRectangle(
        PdfPen(PdfBrushes.get_Red(), 0.9), rec)
    
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
      


