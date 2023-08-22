from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/SetExportValueForCheckbox.pdf"
outputFile = "SetExportValueForCheckbox_out.pdf"
      
#Load a pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
count = 1
#Find the field 
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfCheckBoxWidgetFieldWidget):
            checkbox = field if isinstance(field, PdfCheckBoxWidgetFieldWidget) else None
            #Set export value for checkbox
            count+=1
            checkbox.SetExportValue("True" + str(count))
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()
