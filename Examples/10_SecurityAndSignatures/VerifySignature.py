from spire.pdf import *

def WriteAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s)
    fp.close()

inputFile = "./Demos/Data/ExtractImageFromSignature.pdf"
outputFile = "VerifySignature.txt"

# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Access the form in the document
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)

signatures = []
texts = []

# Check if there are any form fields in the document
if formWidget.FieldsWidget.Count > 0:
    # Loop through each form field
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        # Verify that the field is a PdfField instance
        if isinstance(field, PdfField):
            # Convert the field to a signature field widget
            signatureField = PdfSignatureFieldWidget(field)
            # Get the full name of the signature field
            fullName = signatureField.FullName
            # Verify the signature
            valid = doc.VerifySignature(fullName)
            # Determine the validation status text based on the verification result
            if valid:
                text = "The signature is valid"+"\r\n"
            else:
                text = "The signature is invalid"+"\r\n"
            # Append the text to the list
            texts.append(text)

# Write the result to a text file
WriteAllText(outputFile, texts)