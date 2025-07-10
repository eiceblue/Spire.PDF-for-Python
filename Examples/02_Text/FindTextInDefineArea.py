from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
outputFile = "FindTextInDefineArea.pdf"


# Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Define a rectangle to specify the search area
rctg = RectangleF(0.0, 0.0, 300.0, 300.0)

# Get the first page of the document
pdfPageBase = doc.Pages.get_Item(0)

# Create a PdfTextFinder object for the page
finds = PdfTextFinder(pdfPageBase)

# Set the search parameter to find whole word matches
finds.Options.Parameter = TextFindParameter.WholeWord

# Set the search area to the defined rectangle
finds.Options.Area = rctg

# Find instances of the word "Spire" within the specified rectangle
result = finds.Find("Spire")

# Highlight the found text in green
for find in result:
    find.HighLight(Color.get_Green())

# Find instances of the word "PDF" within the specified rectangle
result2 = finds.Find("PDF")

# Highlight the found text in yellow
for find in result2:
    find.HighLight(Color.get_Yellow())

# Save the modified document to a new file
doc.SaveToFile(outputFile, FileFormat.PDF)

# Close the document
doc.Close()
