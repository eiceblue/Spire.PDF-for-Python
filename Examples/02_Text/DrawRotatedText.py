from spire.pdf.common import *
from spire.pdf import *

outputFile = "DrawRotatedText.pdf"

doc = PdfDocument()
page = doc.Pages.Add()
font = PdfTrueTypeFont("Arial", 12.0,PdfFontStyle.Regular,True)
color = PdfRGBColor(Color.get_Blue())
brush = PdfSolidBrush(color)
text = "This is a text"
page.Canvas.DrawString(text, font, brush, 20.0, 30.0)
state = page.Canvas.Save()
# Rotate 90 degrees clockwise
point1 = PointF(20.0, 30.0)
page.Canvas.RotateTransform(90.0, point1)
page.Canvas.DrawString(text, font, brush, 20.0, 30.0)
page.Canvas.Restore(state)
# Redrawing a new text requires initializing a new state
state2 = page.Canvas.Save()
point2 = PointF(20.0, 150.0)
page.Canvas.RotateTransform(-90.0, point2)
# Rotate 90 degrees counterclockwise
page.Canvas.DrawString(text, font, brush, 20.0, 150.0)
page.Canvas.Restore(state2)        
doc.SaveToFile(outputFile)
doc.Close()