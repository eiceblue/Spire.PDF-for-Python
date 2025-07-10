from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "RemovePageMargins.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Creates a new page
newDoc = PdfDocument()
# Get page margins of source pdf page
margins = doc.PageSettings.Margins
top = margins.Left
bottom = margins.Bottom
left = margins.Left
right = margins.Right
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Adds a new page to the new document
    newPage = newDoc.Pages.Add(SizeF(page.Size.Width - left - right, page.Size.Height - top - bottom), PdfMargins(0.0))
    # Draws the content of the source page onto the new document page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(-left, -top))
#Save the document
newDoc.SaveToFile(outputFile)
newDoc.Close()
doc.Close()

