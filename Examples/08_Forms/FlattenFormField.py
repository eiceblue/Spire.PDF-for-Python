from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/FlattenFormField.pdf"
outputFile = "FlattenFormField_out.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Flatten form fields
doc.Form.IsFlatten = True
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()

