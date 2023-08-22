from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/pdfTemplate_N.pdf"
outputFile = "AddDateTimeStamp.pdf"

#Load a Pdf document from disk
document = PdfDocument()
document.LoadFromFile(inputFile)
#Get the first page
page = document.Pages[0]
#Set the font and brush
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
#Time text
timeString = DateTime.get_Now().ToString("MM/dd/yy hh:mm:ss tt ")
#Create a template and rectangle, draw the string
template = PdfTemplate(140.0, 15.0)
rect = RectangleF(PointF(page.ActualSize.Width - template.Width - 10, page.ActualSize.Height - template.Height - 10), template.Size)
template.Graphics.DrawString(timeString, font, brush, PointF(0.0, 0.0))
#Create stamp annoation
stamp = PdfRubberStampAnnotation(rect)
apprearance = PdfAppearance(stamp)
apprearance.Normal = template
stamp.Appearance = apprearance
page.AnnotationsWidget.Add(stamp)
#Sabe the document
document.SaveToFile(outputFile, FileFormat.PDF)
document.Close()

