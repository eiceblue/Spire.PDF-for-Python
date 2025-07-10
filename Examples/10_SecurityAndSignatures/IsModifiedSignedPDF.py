from spire.pdf import *

def WriteAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s)
    fp.close()

inputFile = "./Demos/Data/ExtractImageFromSignature.pdf"
outputFile = "IsModifiedSignedPDF.txt"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Access the form in the document
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)

text = ""
modified = False

# Check if there are any form fields in the document
if formWidget.FieldsWidget.Count > 0:
    # Loop through each form field
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        # Verify that the field is a PdfField instance
        if isinstance(field, PdfField):
            # Convert the field to a signature field widget
            signatureField = PdfSignatureFieldWidget(field)
            # Get the signature object associated with the signature field
            signatureOne = signatureField.Signature
            # Verify if the document was modified
            modified = signatureOne.VerifyDocModified()
            break

# Determine the final text message based on the modified flag
if modified:
    text = "The document was modified"
else:
    text = "The document was not modified"

# Write the result to a text file
WriteAllText(outputFile, text)