from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ExpandSpecificBookmarks.pdf"
outputFile = "ExpandSpecificBookmarks.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Set BookMarkExpandOrCollapse as "true" for the first bookmarks 
pdf.Bookmarks.get_Item(0).ExpandBookmark = True
#Set BookMarkExpandOrCollapse as "false" for the second bookmarks 
pdf.Bookmarks.get_Item(1).ExpandBookmark = False
#Save the file
pdf.SaveToFile(outputFile)
pdf.Close()

