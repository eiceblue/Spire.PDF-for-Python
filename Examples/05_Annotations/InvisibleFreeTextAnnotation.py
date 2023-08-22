from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_4.pdf"
outputFile = "InvisibleFreeTextAnnotation.pdf"

#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get the first page of PDF file.
page = doc.Pages[0]
#Add a free text annotation to the page and set it invisible.
rect = RectangleF(100.0, 120.0, 150.0, 30.0)
FreetextAnnotation = PdfFreeTextAnnotation(rect)
FreetextAnnotation.Text = "Invisible Free Text Annotation"
font = PdfFont(PdfFontFamily.TimesRoman, 10.0)
border = PdfAnnotationBorder(1.0)
FreetextAnnotation.Font = font
FreetextAnnotation.Border = border
FreetextAnnotation.BorderColor = PdfRGBColor(Color.get_Purple())
FreetextAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
FreetextAnnotation.Color = PdfRGBColor(Color.get_Green())
FreetextAnnotation.Opacity = 0.8
#Invisible free text annotation.
FreetextAnnotation.pipeFlags(PdfAnnotationFlags.Print.value | PdfAnnotationFlags.NoView.value)
page.AnnotationsWidget.Add(FreetextAnnotation)
#Add a free text annotation show it on the page.
rect = RectangleF(100.0, 180.0, 150.0, 30.0)
FreetextAnnotation = PdfFreeTextAnnotation(rect)
FreetextAnnotation.Text = "Show Free Text Annotation"
FreetextAnnotation.Font = font
FreetextAnnotation.Border = border
FreetextAnnotation.BorderColor = PdfRGBColor(Color.get_LightPink())
FreetextAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
FreetextAnnotation.Color = PdfRGBColor(Color.get_LightGreen())
FreetextAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(FreetextAnnotation)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

