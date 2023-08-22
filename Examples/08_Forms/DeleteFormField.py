from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/DeleteFormField.pdf"
outputFile = "DeleteFormField.pdf"

doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Find the particular form field and delete it
if formWidget.FieldsWidget.Count > 0:
    i = 0
    while i < formWidget.FieldsWidget.Count:
        field = formWidget.FieldsWidget.get_Item(i)

        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            if textbox.Name == "password2":
                formWidget.FieldsWidget.Remove(textbox)
        i = i + 1
#Save the pdf document
doc.SaveToFile(outputFile)
doc.Close()

