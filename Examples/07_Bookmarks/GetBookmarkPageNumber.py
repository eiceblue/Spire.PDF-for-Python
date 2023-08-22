from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"
outputFile = "GetPdfBookmarkPageNumber.txt"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get bookmarks collections of the PDF file.
bookmarks = doc.Bookmarks
#Get the page number of the first bookmark.
bookmark = bookmarks[0]
pageNumber = doc.Pages.IndexOf(bookmark.Destination.Page)+1
#Save to file.
showPageNumber = str(pageNumber)
#Save to file.
with open(outputFile, "w") as file:
    file.write(showPageNumber)
doc.Close()