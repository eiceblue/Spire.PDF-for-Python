from io import FileIO
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ExtractJavaScript.pdf"
outputFile = "ExtractJavaScript.txt"

#Create a pdf document
pdf = PdfDocument()
#Load a pdf document
pdf.LoadFromFile(inputFile)
js = None
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Find the FieldsWidget
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
        #Find the textbox named total
        if textbox.Name == "total":
            #Get the action
            jsa = textbox.Actions.Calculate
            if jsa is not None:
                #Get JavaScript
                js = jsa.Script
#Save the result file
f2=open(outputFile,'w', encoding='UTF-8')
f2.write(js)
f2.close()
pdf.Close()

