from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ButtonField.pdf"
outputFile = "FillImageInButtonField.pdf"
inputImage = "./Demos/Data/E-logo.png"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Traverse all the forms
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfButtonWidgetFieldWidget):
            field = field if isinstance(field, PdfButtonWidgetFieldWidget) else None
            if field.Name == "Button1":
                #Set "true" to fit bounds
                field.IconLayout.IsFitBounds = True
                #Fill the annotation rectangle exactly without its original aspect ratio
                field.IconLayout.ScaleMode = PdfButtonIconScaleMode.Anamorphic
                #Fill an image
                field.SetButtonImage(PdfImage.FromFile(inputImage))                
#Save to a file
pdf.SaveToFile(outputFile, FileFormat.PDF)
pdf.Close()

