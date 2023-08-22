from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/RadioButton.pdf"
outputFile = "SelectRadioButtonItem_out.pdf"

#Load a pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Find the field 
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfRadioButtonListFieldWidget):
            radioButton = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
            if radioButton.Name == "RadioButton":
                radioButton.SelectedIndex = 1
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()

