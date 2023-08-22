from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/TextBoxSampleB.pdf"
outputFile = "SetFontForFormField.pdf"

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
#Set the font for textbox
textbox.Font = PdfTrueTypeFont("Tahoma", 12.0, PdfFontStyle.Regular, True)
#Set text
textbox.Text = "Hello World"
#Save to file
doc.SaveToFile(outputFile)
doc.Close()

