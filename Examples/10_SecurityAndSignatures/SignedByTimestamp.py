from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
inputFile_pfx = "./Demos/Data/gary.pfx"
inputImage="./Demos/Data/E-iceblueLogo.png"
outputFile = "SignedByTimestamp.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a digital signature
signature = Security_PdfSignature(doc, doc.Pages.get_Item(0), inputFile_pfx, "e-iceblue", "signature")

# Set the bounds of the signature box
signature.Bounds = RectangleF(PointF(90.0, 550.0), SizeF(180.0, 90.0))

# Configure signature appearance and details
signature.NameLabel = "Digitally signed by:Gary"
signature.LocationInfoLabel ="Location:"
signature.LocationInfo = "CN"
signature.ReasonLabel = "Reaseon:"
signature.Reason = "Ensure authenticity"
signature.ContactInfoLabel = "Contact Number: "
signature.ContactInfo = "028-81705109"

# Set document permissions
signature.DocumentPermissions = PdfCertificationFlags.AllowFormFill.value | PdfCertificationFlags.ForbidChanges.value

# Set graphic mode for the signature
signature.GraphicsMode = Security_GraphicMode.SignImageAndSignDetail

# Set the signature image
signature.SignImageSource = PdfImage.FromFile(inputImage)

# Configure timestamp URL
url = "https://freetsa.org/tsr"
signature.ConfigureTimestamp(url)

# Save the document
doc.SaveToFile(outputFile)