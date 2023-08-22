
from spire.pdf.common import *
from spire.pdf import *

outputFile = "ZoomToPageContents.pdf"
inputFile = "./Demos/Data/PDFTemplate_N.pdf"

#Load Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Create a newDoc
newDoc = PdfDocument()
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    #Add new page with 'A3' size
    newPage = newDoc.Pages.Add(PdfPageSize.A3(), PdfMargins(0.0,0.0))
    #Zoom content to the new page
    newPage.Canvas.ScaleTransform(newPage.ActualSize.Width / float(page.ActualSize.Width), (newPage.ActualSize.Height / float(page.ActualSize.Height)))
    #Draw the page to new page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(0.0, 0.0))
#Save the Pdf document
newDoc.SaveToFile(outputFile, FileFormat.PDF)
newDoc.Close()

