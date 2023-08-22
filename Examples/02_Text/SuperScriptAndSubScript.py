from spire.pdf.common import *
from spire.pdf import *


def DrawSuperscript(page, text, font, brush):
        x = 120.0
        y = 100.0
        page.Canvas.DrawString(text, font, brush, PointF(x, y))

        #Measure the string
        size = font.MeasureString(text)

        #Set the x coordinate of the superscript text
        x += size.Width

        #Instantiate a PdfStringFormat instance
        strformat = PdfStringFormat()

        #Set format as superscript
        strformat.SubSuperScript = PdfSubSuperScript.SuperScript

        #Draw superscript text with format
        text = "Superscript"
        page.Canvas.DrawString(text, font, brush, PointF(x, y), strformat)

def DrawSubscript(page, text, font, brush):
        x = 120.0
        y = 150.0
        page.Canvas.DrawString(text, font, brush, PointF(x, y))

        #Measure the string
        size = font.MeasureString(text)

        #Set the x coordinate of the superscript text
        x += size.Width

        #Instantiate a PdfStringFormat instance
        strformat = PdfStringFormat()

        #Set format as superscript
        strformat.SubSuperScript = PdfSubSuperScript.SubScript

        #Draw superscript text with format
        text = "SubScript"
        page.Canvas.DrawString(text, font, brush, PointF(x, y), strformat)


result = "SuperScriptAndSubScriptInPDF_out.pdf"
#Create a pdf document
doc = PdfDocument()
#Add a page
page = doc.Pages.Add()

#Set font and brush
font = PdfTrueTypeFont("Arial", 20.0,PdfFontStyle.Regular,True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))

text = "Spire.PDF for Python"

#Draw Superscript
DrawSuperscript(page, text, font, brush)

#Draw Subscript
DrawSubscript(page, text, font, brush)


#Save the document
doc.SaveToFile(result)
doc.Close()

    
