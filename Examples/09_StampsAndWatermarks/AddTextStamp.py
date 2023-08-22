from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/AddTextStamp.pdf"
outputFile = "AddTextStamp_out.pdf"

#Open a pdf document
document = PdfDocument()
document.LoadFromFile(inputFile)
#Get the first page
page = document.Pages[0]
#Create a pdf template
template = PdfTemplate(125.0, 55.0)
font1 = PdfTrueTypeFont("Elephant", 10.0, PdfFontStyle.Italic, True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkRed()))
pen = PdfPen(brush)
rectangle = RectangleF(PointF(5.0, 5.0), template.Size)
CornerRadius = 20.0
path = PdfPath()
path.AddArc(template.GetBounds().X, template.GetBounds().Y, CornerRadius, CornerRadius, 180.0, 90.0)
path.AddArc(template.GetBounds().X + template.Width - CornerRadius, template.GetBounds().Y, CornerRadius, CornerRadius, 270.0, 90.0)
path.AddArc(template.GetBounds().X + template.Width - CornerRadius, template.GetBounds().Y + template.Height - CornerRadius, CornerRadius, CornerRadius, 0.0, 90.0)
path.AddArc(template.GetBounds().X, template.GetBounds().Y + template.Height - CornerRadius, CornerRadius, CornerRadius, 90.0, 90.0)
path.AddLine(template.GetBounds().X, template.GetBounds().Y + template.Height - CornerRadius, template.GetBounds().X, template.GetBounds().Y + CornerRadius / float(2))
template.Graphics.DrawPath(pen, path)
#Draw stamp text
s1 = "REVISED\n"
s2 = "by E-iceblue at " + DateTime.get_Now().ToString("MM dd, yyyy")
template.Graphics.DrawString(s1, font1, brush, PointF(5.0, 10.0))
font2 = PdfTrueTypeFont("Lucida Sans Unicode", 9.0, PdfFontStyle.Bold, True)
template.Graphics.DrawString(s2, font2, brush, PointF(2.0, 30.0))
#Create a rubber stamp
stamp = PdfRubberStampAnnotation(rectangle)
apprearance = PdfAppearance(stamp)
apprearance.Normal = template
stamp.Appearance = apprearance
#Draw stamp into page
page.AnnotationsWidget.Add(stamp)
#Save pdf document
document.SaveToFile(outputFile)
document.Close()

