from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_1.pdf"
outputFile = "GetPdfChildBookmarks_out.txt"

def GetChildBookmarks( bookmarks, result):
    #Declare a new StringBuilder content
    content = []
    #Get Pdf child Bookmarks information.
    for i in range(bookmarks.Count):
        parentBookmark = bookmarks.get_Item(i)
        cldBk = PdfBookmarkCollection(parentBookmark)
        if cldBk.Count > 0:
            content.append("Child Bookmarks:")
            for j in range(cldBk.Count):
                childBookmark = cldBk.get_Item(j)
                #Get the title
                content.append(childBookmark.Title)
                #Get the color.
                color = str(childBookmark.Color)
                colorR = color.split(' ')[0][1:len(color.split(' ')[0])]
                content.append(colorR)
				#Get the text style.
                textStyle = str(childBookmark.DisplayStyle)
                content.append(textStyle)
        #Save to file.
        with open(result, "w") as file:
            file.write("\n".join(content))

#Create a new Pdf document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get bookmarks collections of the PDF file.
bookmarks = doc.Bookmarks
#Get Pdf child Bookmarks.
GetChildBookmarks(bookmarks, outputFile)
doc.Close()




