from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/UpdateBookmark.pdf"
outputFile = "UpdateBookmark.pdf"

def EditChildBookmark(parentBookmark):
    pBookmark = PdfBookmarkCollection(parentBookmark)
    for i in range(pBookmark.Count):
        childBookmark = pBookmark.get_Item(i)
        childBookmark.Color = PdfRGBColor(Color.get_Blue())
        childBookmark.DisplayStyle = PdfTextStyle.Regular
        EditChild2Bookmark(childBookmark)
def EditChild2Bookmark(childBookmark):
    cldBookmark = PdfBookmarkCollection(childBookmark)
    for i in range(cldBookmark.Count):
        child2Bookmark = cldBookmark.get_Item(i)
        child2Bookmark.Color = PdfRGBColor(Color.get_LightSalmon())
        child2Bookmark.DisplayStyle = PdfTextStyle.Italic


#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first bookmark
bookmark = doc.Bookmarks[0]
#Change the title of the bookmark
bookmark.Title = "Modified BookMark"
#Set the color of the bookmark
bookmark.Color = PdfRGBColor(Color.get_Black())
#Set the outline text style of the bookmark
bookmark.DisplayStyle = PdfTextStyle.Bold
#Edit child bookmarks of the parent bookmark
EditChildBookmark(bookmark)
#Save the pdf document
doc.SaveToFile(outputFile)
doc.Close()


