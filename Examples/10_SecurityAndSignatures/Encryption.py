from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
inputFile_pfx = "./Demos/Data/gary.pfx"
outputFile = "Encryption.pdf"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a security policy with user and owner passwords
securityPolicy = PdfPasswordSecurityPolicy("open", "test")

# Set the encryption algorithm
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.RC4_128

# Define document privileges
dp = PdfDocumentPrivilege.ForbidAll()
dp.AllowPrint = True
dp.AllowFillFormFields = True
securityPolicy.DocumentPrivilege = dp

# Encrypt the document with the security policy
doc.Encrypt(securityPolicy)

# Save the document
doc.SaveToFile(outputFile)