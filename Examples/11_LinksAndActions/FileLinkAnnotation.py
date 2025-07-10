from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "FileLinkAnnotation.pdf"

def AddFileLinkAnnotation(page, y):
    #Define a font
    font = PdfTrueTypeFont("Arial", 12.0,PdfFontStyle.Regular,True)
    #Set the string format 
    format = PdfStringFormat(PdfTextAlignment.Left)
    #Text string
    prompt = "Launch a File: "
    #Draw text string on page canvas
    page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
    #Use MeasureString to get the width of string
    x = font.MeasureString(prompt, format).Width
    #String of file name
    label = "Sample.pdf"
    #Use MeasureString to get the SizeF of string
    size = font.MeasureString(label)
    #Create a rectangle
    bounds = RectangleF(x, y, size.Width, size.Height)
    #Draw label string
    page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
    #Create PdfFileLinkAnnotation on the rectangle and link file "Sample.pdf"
    annotation = PdfFileLinkAnnotation(bounds, inputFile)
    #Set color for annotation
    annotation.Color = PdfRGBColor(Color.get_Blue())
    #Add annotation to the page
    newPage = PdfNewPage(page.Ptr)
    newPage.Annotations.Add(annotation)

#Create a pdf document
doc = PdfDocument()
#Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
#Setting for page margin
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Add one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
#Define a PdfBrush
brush1 = PdfBrushes.get_Black()
#Define a font
font1 = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Bold, True)
#Set the string format 
format1 = PdfStringFormat(PdfTextAlignment.Left)
#Set the position for drawing 
x = 0.0
y = 50.0
#Text string 
specification = "The sample demonstrates how to create a file link in PDF document."
#Draw text string on page canvas
page.Canvas.DrawString(specification, font1, brush1, x, y, format1)
#Use MeasureString to get the height of string
y = y + font1.MeasureString(specification, format1).Height + 10
#Add file link annotation
AddFileLinkAnnotation(page, y)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()