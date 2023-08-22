from spire.pdf.common import *
from spire.pdf import *

outputFile = "DrawWithGradient-result.pdf"

#Create a pdf document
doc = PdfDocument()
#Add a new page
page = doc.Pages.Add()
#Create a rectangle
rect = RectangleF(PointF(0.0, 0.0), SizeF(300.0, 100.0))
#Create a brush with gradient
brush = PdfLinearGradientBrush(rect, PdfRGBColor(Color.get_Red()), PdfRGBColor(Color.get_Blue()), PdfLinearGradientMode.Horizontal)
#Create a true type font with size 20f, underline style
font = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Underline,True)
#Draw text
page.Canvas.DrawString("Welcome to E-iceblue!", font, brush, PointF(0.0, 100.0))
#Save to file
doc.SaveToFile(outputFile)
doc.Close()

