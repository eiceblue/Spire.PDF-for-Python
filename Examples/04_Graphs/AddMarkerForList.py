from spire.pdf import *

# Path to the input image file
inputFile_Img = "./Demos/Data/E-logo.png"  
# Path to the output PDF file
outputFile = "AddMarkerForList.pdf"  

# Create a new PdfDocument
doc = PdfDocument()

# Add a new page to the document
page = doc.Pages.Add()

# Create a PdfMarker object with a custom image marker style
marker = PdfMarker(PdfUnorderedMarkerStyle.CustomImage)

# Set the image for the marker from the specified input file
marker.Image = PdfImage.FromFile(inputFile_Img)

# Define the content for the list
listContent = "Data Structure\n"
listContent += "Algorithm\n"
listContent += "Computer Networks\n"
listContent += "Operating System\n"
listContent += "C Programming\n"
listContent += "Computer Organization and Architecture"

# Create a PdfList object with the specified content
list = PdfList(listContent)

# Set the indentation for the list
list.Indent = 2

# Set the text indentation for the list
list.TextIndent = 4

# Set the marker for the list using the custom image marker
list.Marker = marker

# Draw the list on the page at the specified coordinates
list.Draw(page.Canvas, 100, 100)

# Save the document to the specified output file
doc.SaveToFile(outputFile, FileFormat.PDF)

# Close the document
doc.Close()