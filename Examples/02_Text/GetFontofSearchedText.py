from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

# Define the path to the input PDF file
inputfile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "GetFontofSearchedText_out.txt"

# Create a PDF document object
doc = PdfDocument()

# Load the PDF file into the document object
doc.LoadFromFile(inputfile)

# Get the first page of the PDF document
page = doc.Pages.get_Item(0)

# Create a PdfTextFinder object
finder = PdfTextFinder(page)

# Search for all occurrences of the text "Spire.PDF for Python" in the page
fragments = finder.Find("Spire.PDF for Python")

# Initialize an empty list to store the formatted output strings
sb = []

# Iterate over each found text fragment
for fragment in fragments:
    sb.append("------------------------------" + "\n")

    # Append the font name
    sb.append(fragment.TextStates[0].FontName + "\n")

    # Round the font size to 2 decimal places and convert it to a string, then append it
    sb.append(str(round(fragment.TextStates[0].FontSize, 2)) + "\n")

# Write the details of the searched text to a file
WriteAllText(outputFile, sb)

# Close the document to free up resources
doc.Close()

