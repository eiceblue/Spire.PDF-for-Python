from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/FormField.pdf"
outputFile = "ModifyFormFieldValue_out.pdf"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            #Find the textbox named total
            if textbox.Name == "TextBox1":
                textbox.Text = "New value"
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()

