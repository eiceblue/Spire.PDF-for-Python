from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"

#Create a new Pdf document.
document = PdfDocument()
#Load the file from disk.
document.LoadFromFile(inputFile)
#Remove all bookmarks.
document.Bookmarks.Clear()
result = "DeleteAllBookmarks.pdf"
#Save the document
document.SaveToFile(result)
document.Close()

