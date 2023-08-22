from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/MultipagePDF.pdf"
outputFile = "PageNumberInFooter.pdf"

def DrawPageNumber(doc, margin, startNumber, pageCount):
    for i in range(doc.Pages.Count):
        page = doc.Pages.get_Item(i)
        page.Canvas.SetTransparency(0.5)
        brush = PdfBrushes.get_Black()
        pen = PdfPen(brush, 0.75)
        font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Italic, True)
        format = PdfStringFormat(PdfTextAlignment.Right)
        format.MeasureTrailingSpaces = True
        space = font.Height * 0.75
        x = margin.Left
        width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
        y = page.Canvas.ClientSize.Height - margin.Bottom + space
        page.Canvas.DrawLine(pen, x, y, x + width, y)
        y = y + 1
        numberLabel = "{0:d} of {1:d}".format(startNumber, pageCount)
        startNumber += 1
        page.Canvas.DrawString(numberLabel, font, brush, x + width, y, format)
        page.Canvas.SetTransparency(1.0)

def DrawPageNumber(doc, margin, startNumber, pageCount):
    for i in range(doc.Pages.Count):
        page = doc.Pages.get_Item(i)
        page.Canvas.SetTransparency(0.5)
        brush = PdfBrushes.get_Black()
        pen = PdfPen(brush, 0.75)
        font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Italic, True)
        format = PdfStringFormat(PdfTextAlignment.Right)
        format.MeasureTrailingSpaces = True
        space = font.Height * 0.75
        x = margin.Left
        width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
        y = page.Canvas.ClientSize.Height - margin.Bottom + space
        page.Canvas.DrawLine(pen, x, y, x + width, y)
        y = y + 1
        numberLabel = "{0:d} of {1:d}".format(startNumber, pageCount)
        startNumber += 1
        page.Canvas.DrawString(numberLabel, font, brush, x + width, y, format)
        page.Canvas.SetTransparency(1.0)


#Create a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Set the margin
margin = doc.PageSettings.Margins
#Draw Page number
DrawPageNumber(doc, margin, 1, doc.Pages.Count)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()


   