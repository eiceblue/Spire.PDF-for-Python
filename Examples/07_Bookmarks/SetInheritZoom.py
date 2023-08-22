from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"
outputFile = "SetInheritZoom_out.pdf"

#Create a new PDF document
pdfdoc = PdfDocument()
#load the document from disk
pdfdoc.LoadFromFile(inputFile)
#Get bookmarks collections of the PDF file
bookmarks = pdfdoc.Bookmarks
#Set Zoom level as 0, which the value is inherit zoom
for i in range(bookmarks.Count):
    bookMark = bookmarks.get_Item(i)
    bookMark.Destination.Zoom = 0.5
#Save the document
pdfdoc.SaveToFile(outputFile)
pdfdoc.Close()

