from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/AddImageStamp.pdf"
outputFile = "AddImageStamp.pdf"

#Load a pdf document
document = PdfDocument()
document.LoadFromFile(inputFile)
#Get the first page
page = document.Pages[0]
#Create a rubber stamp annotation
loStamp = PdfRubberStampAnnotation(RectangleF(PointF(0.0, 0.0), SizeF(60.0, 60.0)))
#Create an instance of PdfAppearance 
loApprearance = PdfAppearance(loStamp)
image = PdfImage.FromFile("./Demos/Data/image stamp.jpg")
template = PdfTemplate(210.0, 210.0)
#Draw a pdf image into pdf template
template.Graphics.DrawImage(image, 60.0, 60.0)
loApprearance.Normal = template
loStamp.Appearance = loApprearance
#Add the rubber stamp annotation into pdf
page.AnnotationsWidget.Add(loStamp)
#Save pdf document
document.SaveToFile(outputFile)
document.Close()

