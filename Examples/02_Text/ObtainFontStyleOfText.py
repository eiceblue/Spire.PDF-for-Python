from spire.pdf.common import *
from spire.pdf import *

# Helper function to write a list of strings to a file.
def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

# Define the path to the input PDF file
inputFile = "data/SampleB_1.pdf"

# Initialize a new PdfDocument object
doc = PdfDocument()

# Load the PDF document from the specified file path on the disk
doc.LoadFromFile(inputFile)

# Define a rectangular area for text searching using RectangleF (x, y, width, height)
# Coordinates are typically in points (1/72 inch)
rctg = RectangleF(0.0, 0.0, 200.0, 300.0)

# Get the first page of the document (index 0)
pdfPageBase = doc.Pages.get_Item(0)

# Initialize the PdfTextFinder with the specific page base
finder = PdfTextFinder(pdfPageBase)

# Set the search parameter to 'none' (default behavior)
finder.Options.Parameter = TextFindParameter.none

# Restrict the search area to the defined rectangle 'rctg'
finder.Options.Area = rctg

# Execute the search and retrieve all text fragments found within the specified area
findouts = finder.FindAllText()

# Initialize a list to store the formatted output strings
builder = []

# Iterate through each found text fragment
for fragment in findouts:
    # Append the extracted text content
    builder.append("Text: " + fragment.Text + "\n")
    
    # Append the font name of the first text state associated with this fragment
    builder.append("FontName: " + fragment.TextStates[0].FontName + "\n")
    
    # Append the font size (rounded to 2 decimal places) of the first text state
    builder.append("FontSize: " + str(round(fragment.TextStates[0].FontSize, 2)) + "\n")

# Write the collected text details (content, font name, font size) to an output file
WriteAllText("ObtainFontStyleOfText.txt", builder)

# Close the PDF document to release resources
doc.Close()

