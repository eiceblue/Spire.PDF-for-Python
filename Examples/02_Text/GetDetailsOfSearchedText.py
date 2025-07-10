from spire.pdf.common import *
from spire.pdf import *


def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "GetDetailsOfSearchedText_out.txt"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the matched phrases
finds =PdfTextFinder(page)
finds.Options.Parameter =TextFindParameter.IgnoreCase
result=finds.Find("Spire.PDF for Python")
# Create a StringBuilder object to put the details of the text searched
builder = []

for find in result:
    builder.append("==================================================================================" + "\n")
    # Append the found text
    builder.append("Text: " + find.Text + "\n")
    # Append the size of the found text
    builder.append("Size: Width=" + str(find.Sizes[0].Width) + ", Height=" + str(find.Sizes[0].Height) + "\n")
    # Append the position of the found text
    builder.append("Position: X=" + str(find.Positions[0].X) + ", Y=" + str(find.Positions[0].Y) + "\n")
    # Append the line that contains the searched text
    builder.append("The line that contains the searched text: " + find.LineText + "\n")

# Write the details of the searched text to a file
WriteAllText(outputFile, builder)

# Close the document
doc.Close()

