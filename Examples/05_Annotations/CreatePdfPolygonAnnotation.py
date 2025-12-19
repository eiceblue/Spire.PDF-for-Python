from spire.pdf.common import *
from spire.pdf import *
from datetime import datetime

outputFile = "CreatePdfPolygonAnnotation_out.pdf"

#Create a Pdf document.
pdf = PdfDocument()
#Add a new page to it.
page = pdf.Pages.Add()
#Initialize an instance of PdfPolygonAnnotation, specifying all vertex coordinates which can form a complete shape.
polygon = PdfPolygonAnnotation(page, [PointF(0.0, 30.0), PointF(30.0, 15.0), PointF(60.0, 30.0), PointF(45.0, 50.0), PointF(15.0, 50.0), PointF(0.0, 30.0)])
#Set the border color, text, border effect and other properties of polygon annotation.
polygon.Color = PdfRGBColor(Color.get_PaleVioletRed())
polygon.Text = "This is a polygon annotation"
polygon.Author = "E-ICEBLUE"
polygon.Subject = "polygon annotation demo"
polygon.BorderEffect = PdfBorderEffect.BigCloud
polygon.ModifiedDate = datetime.now()
#Add the annotation to Pdf page and save the document.
page.AnnotationsWidget.Add(polygon)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()
