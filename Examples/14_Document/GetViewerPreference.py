from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "GetViewerPreference.txt"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
viewer = doc.ViewerPreferences
# Create a StringBuilder object to put the details
builder = []
builder.append("Whether the documents window position is in the center: ")
builder.append("CenterWindow: " + str(viewer.CenterWindow))
builder.append("Document displaying mode, i.e. show thumbnails, full-screen, show attachment panel: ")
builder.append("PageMode: " + str(viewer.PageMode))
builder.append("The page layout, i.e. single page, one column: ")
builder.append("PageLayout: " + str(viewer.PageLayout))
builder.append("Whether window's title bar should display document title: ")
builder.append("DisplayTitle: " + str(viewer.DisplayTitle))
builder.append("Whether to resize the document's window to fit the size of the firstdisplayed page: ")
builder.append("FitWindow:" + str(viewer.FitWindow))
builder.append("Whether to hide menu bar of the viewer application: ")
builder.append("HideMenubar: " + str(viewer.HideMenubar))
builder.append("Whether to hide tool bar of the viewer application: ")
builder.append("HideToolbar: " + str(viewer.HideToolbar))
builder.append("Whether to hide UI elements like scroll bars and leave only the page contents displayed: ")
builder.append("HideWindowUI: " + str(viewer.HideWindowUI))
#save
fp = open(outputFile,"w")
for s in builder:
    fp.write(s + "\n")
fp.close()