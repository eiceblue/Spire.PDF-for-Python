from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/AddFreeTextAnnotation.pdf"
outputFile = "AddFreeTextAnnotation.pdf"

#Create a pdf document
doc = PdfDocument()
doc.LoadFromFile( inputfile)
page = doc.Pages[0]
rect = RectangleF(0.0, 300.0, 100.0, 80.0)
#Add free text annotation
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\n  Spire.PDF"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.TimesRoman, 20.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Gray())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Slash
textAnnotation.Color = PdfRGBColor(Color.get_LightBlue())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 200.0, 150.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nHigh Fidelity Pdf file Conversion"
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
textAnnotation.Text = "\nEasily Manipulate document and Form fields"
border = PdfAnnotationBorder(1.0)
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
textAnnotation.Text = "\nSecurity features"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Pink())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightGreen())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 440.0, 200.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nExtract data from Pdf documents"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_OrangeRed())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightGoldenrodYellow())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()