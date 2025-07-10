from spire.pdf import *

inputFile = "./Demos/Data/CheckPasswordProtection.pdf"
outputFile = "Decryption.pdf"

# Load a PDF document from disk
doc = PdfDocument()

# Use 'test' as the owner password
doc.LoadFromFile(inputFile,"test")

# Decrypt the document
doc.Decrypt()

# # Or you can use 'open' as the user password
# doc.LoadFromFile(inputFile,"open")
# # Decrypt the document using the owner password
# doc.Decrypt("test")

# Save the document
doc.SaveToFile(outputFile)