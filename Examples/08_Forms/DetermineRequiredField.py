from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/DetermineRequiredField.pdf"
outputFile = "DetermineRequiredField.pdf"

doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Find the particular form field and determine if it marks as required or not
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)

        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            if textbox.Name == "username":
                textbox.Required = True
            if textbox.Name == "password2":
                textbox.Required = False
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()
