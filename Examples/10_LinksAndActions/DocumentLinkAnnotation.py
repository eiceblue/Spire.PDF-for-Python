from spire.pdf.common import *
from spire.pdf import *

outputFile = "DocumentLinkAnnotation_out.pdf"

def AddDocumentLinkAnnotation(pdf, AddPage, DestinationPage, y):
    #Define a font
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
    #Set the string format
    format = PdfStringFormat(PdfTextAlignment.Left)
    #Text string
    prompt = "Local document Link: "
    #Draw text string on page that
    pdf.Pages[AddPage].Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
    #Use MeasureString to get the width of string
    x = font.MeasureString(prompt, format).Width
    #Create a PdfDestination with specific page
    dest = PdfDestination(pdf.Pages[DestinationPage])
    #Set the location of destination
    dest.Location = PointF(0.0, y)
    #Set 50% zoom factor
    dest.Zoom = 0.5
    #Label string
    label = "Click here to link the second page."
    #Use MeasureString to get the SizeF of string
    size = font.MeasureString(label)
    #Create a rectangle
    bounds = RectangleF(x, y, size.Width, size.Height)
    #Draw label string
    pdf.Pages[AddPage].Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
    #Create PdfDocumentLinkAnnotation on the rectangle and link to the destination  
    annotation = PdfDocumentLinkAnnotation(bounds, dest)
    #Set color for annotation
    annotation.Color = PdfRGBColor(Color.get_Blue())
    #Add annotation to the page
    addPage = pdf.Pages[AddPage]
    newPage = PdfNewPage(addPage.Ptr)
    newPage.Annotations.Add(annotation)

#Create a pdf document
doc = PdfDocument()
#Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
#Setting for page margin
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(2.0, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Add the first page
page1 = doc.Pages.Add(PdfPageSize.A4(), margin)
#Define a PdfBrush
brush1 = PdfBrushes.get_Black()
#Define a font
font1 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Bold, True)
#Set the string format 
format1 = PdfStringFormat(PdfTextAlignment.Left)
#Set the position for drawing 
x = 0.0
y = 50.0
#Text string 
specification = "The sample demonstrates how to create a local document link in PDF document."
#Draw text string on first page 
page1.Canvas.DrawString(specification, font1, brush1, x, y, format1)
#Use MeasureString to get the height of string
y = y + font1.MeasureString(specification, format1).Height +10
#Add the second page
page2 = doc.Pages.Add(PdfPageSize.A4(), margin)
#String text
PageContent = "This is the second page!"
#Draw text string on second page 
page2.Canvas.DrawString(PageContent, font1, brush1, x, y, format1)
#Add DocumentLinkAnnotation on the first page and link to the second page
AddDocumentLinkAnnotation(doc, 0, 1, y)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()