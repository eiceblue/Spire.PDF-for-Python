from io import FileIO
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/GetStyleOfRadioButton.pdf"
outputFile = "GetStyleOfRadioButton_out.txt"

#Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get the first page
page = pdf.Pages[0]
builder = []
num = 0
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Traverse all the forms
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        #Find the radio button field
        if isinstance(field, PdfRadioButtonListFieldWidget):
            num += 1
            radio = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
            #Get the button style
            buttonStyle = radio.ButtonStyle
            builder.append(("The button style of Radio button {0:d} is: "+str(buttonStyle)).format(num))
#Save the document
f2=open(outputFile,'w', encoding='UTF-8')
for item in builder:
        f2.write("%s\n" % item)
f2.close()
pdf.Close()


