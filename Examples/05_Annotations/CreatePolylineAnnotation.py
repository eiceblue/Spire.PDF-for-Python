from spire.pdf.common import *
from spire.pdf import *
from datetime import datetime

outputFile = "CreatePolylineAnnotation.pdf"

#Create a pdf document
pdf = PdfDocument()
#Add a new page
page = pdf.Pages.Add()
#Create a polyline annotation
polyline = PdfPolyLineAnnotation(page, [PointF(0.0, 60.0), PointF(30.0, 45.0), PointF(60.0, 90.0), PointF(90.0, 80.0)])
#Set properties of polyline
polyline.Color = PdfRGBColor(Color.get_PaleVioletRed())
polyline.Text = "This is a polygon annotation"
polyline.Author = "E-ICEBLUE"
polyline.Subject = "polygon annotation demo"
polyline.Name = "Test Annotation"
polyline.Border = PdfAnnotationBorder(1)
polyline.ModifiedDate = datetime.now()
#Add the annotation into page
page.AnnotationsWidget.Add(polyline)
#Save pdf
pdf.SaveToFile(outputFile, FileFormat.PDF)
pdf.Close()
