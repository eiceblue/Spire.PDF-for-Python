from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/DocumentsLinks.pdf"
inputFile2 = "./Demos/Data/Sample.pdf"
outputFile = "LaunchFileInNewWindow.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile1)
#Define the variables
finds = None
test = ["Spire.PDF"]
#Traverse the pages
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    i = 0
    while i < len(test):
        #Find the defined string
        finds = page.FindText(test[i], TextFindParameter.WholeWord).Finds
        #Traverse the finds
        for find in finds:
            launchAction = PdfLaunchAction(inputFile2, PdfFilePathType.Relative)
            #Set open document in a new window
            launchAction.IsNewWindow = True
            #Add annotation
            rect = RectangleF(find.Position.X, find.Position.Y, find.Size.Width, find.Size.Height)
            annotation = PdfActionAnnotation(rect, launchAction)
            pageWidget = PdfPageWidget(page)
            pageWidget.AnnotationsWidget.Add(annotation)
        i += 1        
#Save the file
pdf.SaveToFile(outputFile)
pdf.Close()