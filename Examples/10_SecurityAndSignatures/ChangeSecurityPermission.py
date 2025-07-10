from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
outputFile = "ChangeSecurityPermission.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Define the security policy for the document
# No user password is set, but an owner password "test" is used
securityPolicy = PdfPasswordSecurityPolicy("", "test")

# Set the encryption algorithm to AES with a 256-bit key length
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_256

# Define document privileges
dp = PdfDocumentPrivilege.ForbidAll()
dp.AllowDegradedPrinting = True
dp.AllowFillFormFields = True

# Assign the document privileges to the security policy
securityPolicy.DocumentPrivilege = dp

# Apply the security policy to the document
doc.Encrypt(securityPolicy)

# Save the document
doc.SaveToFile(outputFile)