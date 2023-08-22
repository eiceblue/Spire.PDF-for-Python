from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "SetExpiryDate.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
javaScript = "var rightNow = new Date();" + "var endDate = new Date('October 20, 2015 23:59:59');" + "if(rightNow.getTime() > endDate)" + "app.alert('This document has expired, please contact us for a new one.',1);" + "this.closeDoc();"
js = PdfJavaScriptAction(javaScript)
doc.AfterOpenAction = js
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

