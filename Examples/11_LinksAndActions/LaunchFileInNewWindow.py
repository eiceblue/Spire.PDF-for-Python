from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/DocumentsLinks.pdf"
inputFile2 = "./Demos/Data/Sample.pdf"
outputFile = "LaunchFileInNewWindow.pdf"


# Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile1)

# Define the variables
# finds = None
test = ["Spire.PDF"]

# Traverse the pages
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    finds =PdfTextFinder(page)
    i = 0
    while i < len(test):
        # Find the defined string
        finds.Options.Parameter =TextFindParameter.WholeWord
        result = finds.Find(test[i])

        # Traverse the finds
        for find in result:
            launchAction = PdfLaunchAction(inputFile2, PdfFilePathType.Relative)

            # Set open document in a new window
            launchAction.IsNewWindow = True
            # Add annotation
            rect =RectangleF(result[0].Positions[0].X, result[0].Positions[0].Y, result[0].Sizes[0].Width, result[0].Sizes[0].Height)
            annotation = PdfActionAnnotation(rect, launchAction)
            pageWidget = PdfPageWidget(page)
            pageWidget.AnnotationsWidget.Add(annotation)
        i += 1
# Save the file
pdf.SaveToFile(outputFile)
pdf.Dispose()


