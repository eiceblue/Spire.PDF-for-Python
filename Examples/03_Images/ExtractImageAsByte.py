from spire.pdf.common import *
from spire.pdf import *

# Define the path to the input PDF file
inputfile = "./Demos/Data/Extraction.pdf"

# Create a PDF document object
doc = PdfDocument()

# Load the PDF file into the document object
doc.LoadFromFile(inputfile)

# Get the first page of the PDF document
page = doc.Pages.get_Item(0)

# Retrieve the information about images on the page
imageInfo = page.ImagesInfo

# Iterate over all images found on the page
for i in range(len(imageInfo)):
    # Construct the output filename for each image
    outputName = "Image-{0:d}.jpg".format(i)

    # Convert the image to a byte array
    byteResult = imageInfo[i].Image.ToArray()

    # Write the byte array to a file, effectively saving the image
    with open(outputName, 'wb') as f:
        f.write(byteResult)

# Close the document to free up resources
doc.Close()
doc.Dispose()

