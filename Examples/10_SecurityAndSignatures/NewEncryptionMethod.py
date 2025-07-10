from spire.pdf import *

inputFile = "./Data/SampleB_1.pdf"
outputFile = "Encryption_new.pdf"

# Load a Pdf document from disk
pdfDocument = PdfDocument()
pdfDocument.LoadFromFile(inputFile)

# Create password security policy
securityPolicy = PdfPasswordSecurityPolicy("123456789", "M123456789")

# Set encryption algorithm
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_128

# Set document permissions (ownership)
securityPolicy.DocumentPrivilege = PdfDocumentPrivilege.ForbidAll()

# Set printing permissions
securityPolicy.DocumentPrivilege.AllowPrint = True
pdfDocument.Encrypt(securityPolicy)

# Save the document
pdfDocument.SaveToFile(outputFile)

pdfDocument.Close()