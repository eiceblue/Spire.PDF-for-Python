
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/PDFTemplate_HF.pdf"
outputFile = "ImageAndTextUsingTemplate.pdf"

#Load Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Get the margins of Pdf
margin = doc.PageSettings.Margins
#Define font and brush
font = PdfTrueTypeFont("Impact",14.0,PdfFontStyle.Regular,True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Gray()))
#Load an image
image = PdfImage.FromFile("./Demos/Data/E-iceblueLogo.png")
#Specify the image size
imageSize = SizeF(image.Width / float(2),image.Height / float(2))
#Create a header template
headerTemplate = PdfTemplate(page.ActualSize.Width - margin.Left - margin.Right, imageSize.Height)
#Draw the image in the template
headerTemplate.Graphics.DrawImage(image, PointF(0.0, 0.0),imageSize)
#Create a retangle
rect = headerTemplate.GetBounds()
#string format
format1 = PdfStringFormat(PdfTextAlignment.Right,PdfVerticalAlignment.Middle)
#Draw a string in the template
headerTemplate.Graphics.DrawString("Header", font, brush, rect, format1)
#Create a footer template and draw a text
footerTemplate = PdfTemplate(page.ActualSize.Width - margin.Left - margin.Right, imageSize.Height)
format2 = PdfStringFormat(PdfTextAlignment.Center,PdfVerticalAlignment.Middle)
footerTemplate.Graphics.DrawString("Footer", font, brush, rect, format2)
x = margin.Left
y = 0.0
#Draw the header template on page at specified location
page.Canvas.DrawTemplate(headerTemplate, PointF(x,y))
#Draw the footer template on page at specified location
y = page.ActualSize.Height - footerTemplate.Height - 10
page.Canvas.DrawTemplate(footerTemplate, PointF(x, y))
#Save the document
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
