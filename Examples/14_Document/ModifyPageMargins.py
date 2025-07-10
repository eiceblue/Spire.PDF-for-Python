from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/ModifyPageMargins.pdf"
outputFile = "ModifyPageMargins.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Creates a new pdf document
newDoc = PdfDocument()
# Defines the page margins of the new document
top = 50.0
bottom = 50.0
left = 50.0
right = 50.0
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Adds a new page to the new document and set the page size to be the same as the source document
    newPage = newDoc.Pages.Add(page.Size, PdfMargins(0.0))
    # Set the scale of the new document content
    newPage.Canvas.ScaleTransform((page.ActualSize.Width - left - right) / page.ActualSize.Width, (page.ActualSize.Height - top - bottom) / page.ActualSize.Height)
    # Draws the content of the source page onto the new document page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(left, top))
#Save the document
newDoc.SaveToFile(outputFile)
newDoc.Close()
doc.Close()

