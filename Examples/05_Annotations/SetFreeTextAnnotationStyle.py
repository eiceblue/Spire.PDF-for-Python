from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Template_Pdf_4.pdf"
outputFile = "SetFreeTextAnnotationFormatting.pdf"

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
textAnnotation.Text = "\nFree Text Annotation Formatting"
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
rect = RectangleF(150.0, 200.0, 150.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nFree Text Annotation Formatting"
border = PdfAnnotationBorder(1.0)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_LightGoldenrodYellow())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightPink())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 280.0, 280.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\noHow to Set Free Text Annotation Formatting in Pdf file"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Gray())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
textAnnotation.Color = PdfRGBColor(Color.get_LightSkyBlue())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 360.0, 200.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nFree Text Annotation Formatting"
border = PdfAnnotationBorder(1.0)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Pink())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightGreen())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
