from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/text.txt"
outputFile = "AddPdfLaunchAction.pdf"

#Create a new PDF document
doc = PdfDocument()
page = doc.Pages.Add()
#Create a PDF Launch Action       
launchAction = PdfLaunchAction(inputFile)
#Create a PDF Action Annotation with the PDF Launch Action
text = "Click here to open file"
font = PdfTrueTypeFont("Arial", 13.0,PdfFontStyle.Regular,True)
rect = RectangleF(50.0, 50.0, 230.0, 15.0)
page.Canvas.DrawString(text, font, PdfBrushes.get_ForestGreen(), rect)
annotation = PdfActionAnnotation(rect, launchAction)
#Add the PDF Action Annotation to page
newPage = PdfNewPage(page.Ptr)
newPage.Annotations.Add(annotation)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()