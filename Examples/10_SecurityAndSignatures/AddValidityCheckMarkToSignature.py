from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
inputFile_pfx = "./Demos/Data/gary.pfx"
outputFile = "AddValidityCheckMarkToSignature.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a signature maker object for the loaded document using the PFX file and password
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")

# Disable Acro6 layers in the signature
signatureMaker.SetAcro6Layers(False)

# Add the invisible signature to the first page of the document at the specified coordinates
signatureMaker.MakeSignature("signName",doc.Pages.get_Item(0),100.0,100.0,120.0,160.0)

# Save the document
doc.SaveToFile(outputFile)