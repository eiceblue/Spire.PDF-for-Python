from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/DeleteBookmark.pdf"
outputFile = "DeleteBookmark.pdf"

#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Delete the first bookmark
doc.Bookmarks.RemoveAt(0)
#Save the pdf document
doc.SaveToFile(outputFile)
doc.Close()

