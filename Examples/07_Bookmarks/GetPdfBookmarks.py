from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"
outputFile = "GetPdfBookmarks.txt"

def GetChildBookmark(parentBookmark, content):
    if parentBookmark.Count > 0:
        #for childBookmark in parentBookmark:
        for i in range(parentBookmark.Count):
            childBookmark = parentBookmark.get_Item(i)
            #Get the title.
            content.append(childBookmark.Title)
            #Get the text style.
            textStyle = str(childBookmark.DisplayStyle)
            content.append(textStyle)
            cldBk = PdfBookmarkCollection(childBookmark)
            GetChildBookmark(cldBk, content)
        
def GetBookmarks(bookmarks, result):
    #Declare a new StringBuilder content
    content = []
    #Get Pdf bookmarks information.
    if bookmarks.Count > 0:
        content.append("Pdf bookmarks:")
        for i in range(bookmarks.Count):
            parentBookmark = bookmarks.get_Item(i)
            #for parentBookmark in bookmarks:
            #Get the title.
            content.append(parentBookmark.Title)
            #Get the text style.
            textStyle = str(parentBookmark.DisplayStyle)
            content.append(textStyle)
            cldBk = PdfBookmarkCollection(parentBookmark)
            GetChildBookmark(cldBk, content)

    #Save to file.
    with open(outputFile, "w") as file:
        file.write("\n".join(content))



#Create a new Pdf document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get bookmarks collection of the Pdf file.
bookmarks = doc.Bookmarks
#Get Pdf Bookmarks.
GetBookmarks(bookmarks, outputFile)
doc.Close()




   
