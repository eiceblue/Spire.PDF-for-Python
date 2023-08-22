from spire.pdf.common import *
from spire.pdf import *

outputFile = "CreatePdfLineAnnotation_out.pdf"

#Create a PDF document.
document = PdfDocument()
#Add a new page.
page = document.Pages.Add()
#Create a line annotation.
linePoints = [100, 650, 180, 650]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the first line annotation")
#Set the line border.
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Solid
lineAnnotation.lineBorder.BorderWidth = 1
#Set the line intent.
lineAnnotation.LineIntent = PdfLineIntent.LineDimension
#Set the line style.
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.Butt
lineAnnotation.EndLineStyle = PdfLineEndingStyle.Diamond
#Set the line flag.
lineAnnotation.Flags = PdfAnnotationFlags.Default
#Set the line color.
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Green())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Green())
#Set the leader line.
lineAnnotation.LeaderLineExt = 0
lineAnnotation.LeaderLine = 0
#Add the line annotation to the page.
page.AnnotationsWidget.Add(lineAnnotation)
linePoints = [100, 550, 280, 550]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the second line annotation")
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Underline
lineAnnotation.lineBorder.BorderWidth =2
lineAnnotation.LineIntent = PdfLineIntent.LineArrow
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.Circle
lineAnnotation.EndLineStyle = PdfLineEndingStyle.Diamond
lineAnnotation.Flags = PdfAnnotationFlags.Default
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Pink())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Pink())
lineAnnotation.LeaderLineExt = 0
lineAnnotation.LeaderLine = 0
page.AnnotationsWidget.Add(lineAnnotation)
linePoints = [100, 450, 280, 450]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the third line annotation")
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Beveled
lineAnnotation.lineBorder.BorderWidth = 2
lineAnnotation.LineIntent = PdfLineIntent.LineDimension
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.none
lineAnnotation.EndLineStyle = PdfLineEndingStyle.none
lineAnnotation.Flags = PdfAnnotationFlags.Default
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Blue())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Blue())
lineAnnotation.LeaderLineExt = 1
lineAnnotation.LeaderLine = 1
page.AnnotationsWidget.Add(lineAnnotation)
#Save the document
document.SaveToFile(outputFile)
document.Close()