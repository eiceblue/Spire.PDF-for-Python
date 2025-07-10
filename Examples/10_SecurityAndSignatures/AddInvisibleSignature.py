from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
inputFile_pfx = "./Demos/Data/gary.pfx"
outputFile = "AddInvisibleSignature.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a signature maker object for the loaded document using the PFX file and password
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")

# Make the invisible signature with the specified name
signatureMaker.MakeSignature("signName")

# Save the document
doc.SaveToFile(outputFile)