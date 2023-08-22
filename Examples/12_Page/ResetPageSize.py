from spire.pdf.common import *
from spire.pdf import *


outputFile = "ResetPageSize.pdf"
inputFile = "./Demos/Data/ResetPageSize.pdf"

# Load the document from disk
originalDoc = PdfDocument()
originalDoc.LoadFromFile(inputFile)
# Set the margins
margins = PdfMargins(0.0)
# Create a new pdf document
with PdfDocument() as newDoc:
    scale = 0.8
for i in range(originalDoc.Pages.Count):
    page = originalDoc.Pages.get_Item(i)
    # Use same scale to set width and height
    width = page.Size.Width * scale
    height = page.Size.Height * scale
    # Add new page with expected width and height
    newPage = newDoc.Pages.Add(SizeF(width, height), margins)
    newPage.Canvas.ScaleTransform(scale, scale)
    # Copy content of original page into new page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF.Empty())
    # save the document
newDoc.SaveToFile(outputFile)
newDoc.Close()
