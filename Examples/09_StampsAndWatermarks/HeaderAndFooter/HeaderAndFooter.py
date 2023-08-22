from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/HeaderAndFooter.pdf"
outputFile = "HeaderAndFooter_out.pdf"

#Open the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
brush = PdfBrushes.get_Black()
pen = PdfPen(brush, 0.75)
font = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Italic, True)
rightAlign = PdfStringFormat(PdfTextAlignment.Right)
leftAlign = PdfStringFormat(PdfTextAlignment.Left)
rightAlign.MeasureTrailingSpaces = True
rightAlign.MeasureTrailingSpaces = True
margin = doc.PageSettings.Margins
space = font.Height * 0.75
x = 0.0
y = 0.0
width = 0.0
#Create a new pdf document
newPdf = PdfDocument()
newPage = None
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    #Add new page
    newPage = newPdf.Pages.Add(page.Size,PdfMargins(0.0))
    newPage.Canvas.SetTransparency(0.5)
    x = margin.Left
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    y = margin.Top - space
    #Draw header line
    newPage.Canvas.DrawLine(pen, x, y + 15, x + width, y + 15)
    y = y+10 - font.Height
    #Draw header image into newPage
    newPage.Canvas.SetTransparency(0.5)
    headerImage = PdfImage.FromFile("./Demos/Data/Header.png" )
    newPage.Canvas.DrawImage(headerImage, PointF(0.0, 0.0))
    #Draw header text into newPage
    newPage.Canvas.DrawString("Demo of Spire.Pdf", font, brush, x + width, y, rightAlign)
    #Draw footer image into newPage
    footerImage = PdfImage.FromFile("./Demos/Data/Footer.png")
    newPage.Canvas.DrawImage(footerImage, PointF(0.0, newPage.Canvas.ClientSize.Height - footerImage.PhysicalDimension.Height))
    brush = PdfBrushes.get_DarkBlue()
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Bold, True)
    y = newPage.Canvas.ClientSize.Height - margin.Bottom - font.Height
    #Draw footer text into newPage
    newPage.Canvas.DrawString("Created by E-iceblue Co,.Ltd", font, brush, x, y, leftAlign)
    newPage.Canvas.SetTransparency(1.0)
    #Draw the page into newPage
    newTemplate = page.CreateTemplate()
    template = PdfGraphicsWidget(newTemplate.Ptr)
    template.Draw(newPage.Canvas, PointF(0.0, 0.0))
#Save the document
newPdf.SaveToFile(outputFile)
newPdf.Close()

