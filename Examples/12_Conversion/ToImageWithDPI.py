from spire.pdf.common import *
from spire.pdf import *

inputFile = "Data/ToImage.pdf"

# Open a PDF document by creating a new PdfDocument instance
doc = PdfDocument()

# Load the PDF file from the specified input file path
doc.LoadFromFile(inputFile)

# Save each page of the PDF as an image file
for i in range(doc.Pages.Count):

    # Generate a unique file name for each image using the page index
    fileName = "ToImage-img-{0:d}.png".format(i)

    # Render the i-th page as an image with a resolution of 300x300 DPI and obtain the image object
    with doc.SaveAsImage(i, 300, 300) as imageS:
        # Save the rendered image to disk with the generated file name
        imageS.Save(fileName)

#Close the PDF document to release resources
doc.Close()