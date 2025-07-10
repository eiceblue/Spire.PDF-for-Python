from spire.pdf.common import *
from spire.pdf import *

outputFile = "SetPageOrientation.pdf"
inputFile = "./Demos/Data/scenery.jpg"

#Create a pdf document
doc = PdfDocument()
#Add a section
section = doc.Sections.Add()
#Load a image
image = PdfImage.FromFile(inputFile)
#Check whether the width of the image file is greater than default page width or not
if image.PhysicalDimension.Width > section.PageSettings.Size.Width:
    #Set the orientation as landscape
    section.PageSettings.Orientation = PdfPageOrientation.Landscape
else:
    section.PageSettings.Orientation = PdfPageOrientation.Portrait
#Add a new page with orientation Landscape
page = section.Pages.Add()
#Draw the image on the page
page.Canvas.DrawImage(image,PointF(0.0,0.0))
#Save to file
doc.SaveToFile(outputFile)
doc.Close()
