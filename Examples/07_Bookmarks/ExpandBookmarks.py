from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"
outputFile = "ExpandBookmarks_out.pdf"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Set BookMarkExpandOrCollapse as true to expand the bookmarks.
doc.ViewerPreferences.BookMarkExpandOrCollapse = True
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

