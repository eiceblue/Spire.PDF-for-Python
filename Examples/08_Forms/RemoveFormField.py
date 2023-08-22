from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/RemoveFormField.pdf"
outputFile = "RemoveFormField_out.pdf"
        
#Create a PdfDocument
pdf = PdfDocument()
#Load the input file from disk
pdf.LoadFromFile(inputFile)
#Get form from the document
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
if formWidget is not None:
    i = 0
    while i <= formWidget.FieldsWidget.List.Count - 1:
        #Case 1: Remove the first form field
        if i == 0:
            field = formWidget.FieldsWidget.get_Item(i)
            refield = field if isinstance(field, PdfField) else None
            formWidget.FieldsWidget.Remove(refield)
            break
        i += 1
    #Save the pdf file
    pdf.SaveToFile(outputFile)
    pdf.Close()
