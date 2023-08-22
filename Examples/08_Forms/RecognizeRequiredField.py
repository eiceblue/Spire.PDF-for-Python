from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/RecognizeRequiredField.pdf"
outputFile = "RecognizeRequiredField_out.txt"

#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
builder = []
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfField):
            field = field if isinstance(field, PdfField) else None
            #Judge if the field is required
            if field.Required:
                builder.append("The field named: "+ field.Name + " is required")
#Save the document
f2=open(outputFile,'w', encoding='UTF-8')
for item in builder:
        f2.write("%s\n" % item)
f2.close()
doc.Close()
