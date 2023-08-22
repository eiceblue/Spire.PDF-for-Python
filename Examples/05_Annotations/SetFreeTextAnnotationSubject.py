from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_4.pdf"
outputFile = "SetFreeTextAnnotationSubject.pdf"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get the first page of PDF file.
page = doc.Pages[0]
#Initialize a PdfFreeTextAnnotation.
rect = RectangleF(150.0, 120.0, 150.0, 30.0)
textAnnotation = PdfFreeTextAnnotation(rect)
#Specify content.
textAnnotation.Text = "\nSet free text annotation subject"
#Set subject.
textAnnotation.Subject = "SubjectTest"
#Set free text annotation formatting and add it to page.
font = PdfFont(PdfFontFamily.TimesRoman, 10.0)
border = PdfAnnotationBorder(1.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Purple())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
textAnnotation.Color = PdfRGBColor(Color.get_Green())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

