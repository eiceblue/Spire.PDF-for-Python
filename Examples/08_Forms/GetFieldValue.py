from io import FileIO
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/TextBoxSampleB_1.pdf"
outputFile = "GetFieldValue.txt"

#Create a pdf document
doc = PdfDocument()
#Load from file
doc.LoadFromFile(inputFile)
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Get textbox
field = formWidget.FieldsWidget.get_Item("Text1")
textbox = PdfTextBoxFieldWidget(field.Ptr)
#Get the text of the textbox
text = textbox.Text
content = []
content.append("The value of the field named " + textbox.Name + " is " + text)
#Save the result file
f2=open(outputFile,'w', encoding='UTF-8')
for item in content:
        f2.write("%s\n" % item)
f2.close()
doc.Close()

