from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
inputFile_pfx = "./Demos/Data/gary.pfx"
inputImage="./Demos/Data/E-iceblueLogo.png"
outputFile = "DigitalSignature.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a signature maker with the PDF document and PFX file
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")

# Configure the signature properties
signature = signatureMaker.Signature
signature.Name = "Gary"
signature.ContactInfo = "028-81705109"
signature.Location = "Chengdu"
signature.Reason = "The certificate of this document"

# Create a signature appearance
appearance = PdfSignatureAppearance(signature)
appearance.NameLabel = "Signer: "
appearance.ContactInfoLabel = "ContactInfo: "
appearance.LocationLabel = "Location: "
appearance.ReasonLabel = "Reaseon: "
appearance.SignatureImage = PdfImage.FromFile(inputImage)
appearance.GraphicMode = GraphicMode.SignImageAndSignDetail
appearance.SignImageLayout = SignImageLayout.none

# Apply the signature to the PDF document
signatureMaker.MakeSignature("Signer:", doc.Pages.get_Item(0), 90.0, 550.0, 270.0, 90.0, appearance)

# Save the document
doc.SaveToFile(outputFile)