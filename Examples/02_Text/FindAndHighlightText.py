from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/FindAndHighlightText.pdf"
outputFile = "FindAndHighlightText_out.pdf"

# Load the document from disk
pdf = PdfDocument()

# Load the PDF file
pdf.LoadFromFile(inputFile)

result = None

# Iterate through each page in the PDF
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)

    # Create a PdfTextFinder object for the current page
    finds = PdfTextFinder(page)

    # Set the search parameter to find exact matches
    finds.Options.Parameter = TextFindParameter.none

    # Find instances of the word "science" on the page
    result = finds.Find("science")

    # Iterate through each instance of the word "science" found on the page
    for find in result:
        # Highlight the searched text
        find.HighLight()

# Save the modified document to a new file
pdf.SaveToFile(outputFile, FileFormat.PDF)
pdf.Close()
