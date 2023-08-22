
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/Template_Pdf_3.pdf"
outputFile = "CreatePdfLinkAnnotation_out.pdf"

#Create a new object of PdfDocument.
doc = PdfDocument()
#Add a page to it.
page = doc.Pages.Add()
#Declare two parameters that will be passed to the constructor of PdfFileLinkAnnotation class.
rect = RectangleF(0.0, 40.0, 250.0, 35.0)
#Create a file link annotation based on the two parameters and add the annotation to the new page.
link = PdfFileLinkAnnotation(rect, inputfile)
page.AnnotationsWidget.Add(link)
#Create a free text annotation based on the same RectangleF, specifying the content.
text = PdfFreeTextAnnotation(rect)
text.Text = "Click here! This is a link annotation."
font = PdfFont(PdfFontFamily.Helvetica, 15.0)
text.Font = font
page.AnnotationsWidget.Add(text)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()