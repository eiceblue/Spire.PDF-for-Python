from spire.pdf import *

inputFile = "./Demos/Data/ExtractImageFromSignature.pdf"
outputFile = "ExtractImageFromSignature/"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Access the form in the document
pdfform = doc.Form

# Get the form widget
formWidget = PdfFormWidget(pdfform)
i = 0

# Extract signature images and save them to files
for image in formWidget.ExtractSignatureAsImages:
    filename = outputFile + "Image-" + str(i) + ".png"

    # Save the image to a file
    image.Save(filename)
    i = i + 1

doc.Close