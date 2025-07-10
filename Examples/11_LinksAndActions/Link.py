from spire.pdf.common import *
from spire.pdf import *

outputFile = "link.pdf"

#Create a pdf document.
doc = PdfDocument()
#Set margins
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
y = 100.0
x = 10.0
font = PdfTrueTypeFont("Lucida Sans Unicode", 14.0,PdfFontStyle.Regular,True)
label = "Simple Text Link: "
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
font1 = PdfTrueTypeFont("Lucida Sans Unicode", 14.0, PdfFontStyle.Underline,True)
url1 = "http://www.e-iceblue.com"
page.Canvas.DrawString(url1, font1, PdfBrushes.get_CadetBlue(), x, y)
y = y + font1.MeasureString(url1).Height + 25
label = "Web Link: "
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
text = "E-iceblue home"
link2 = PdfTextWebLink()
link2.Text = text
link2.Url = url1
link2.Font = font1
link2.Brush = PdfBrushes.get_CadetBlue()
link2.DrawTextWebLink(page.Canvas, PointF(x, y))
y = y + font1.MeasureString(text).Height + 30
label = "URI Annonation: "
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
text = "Google"
location = PointF(x, y)
size = font1.MeasureString(text)
linkBounds = RectangleF(location, size)
link3 = PdfUriAnnotation(linkBounds)
link3.Border = PdfAnnotationBorder(0.0)
link3.Uri = "http://www.google.com"
newPage = PdfNewPage(page)
newPage.Annotations.Add(link3)
page.Canvas.DrawString(text, font1, PdfBrushes.get_CadetBlue(), x, y)
y = y + size.Height + 30
label = "URI Annonation Action: "
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
text = "JavaScript Action (Click Me)"
location = PointF(x-2, y-2)
size = font1.MeasureString(text)
size = SizeF(size.Width+5,size.Height+5)
linkBounds = RectangleF(location,size)
link4 = PdfUriAnnotation(linkBounds)
link4.Border = PdfAnnotationBorder(0.75)
link4.Color = PdfRGBColor(Color.get_CadetBlue())
#JavaScript
script = "app.alert({" + "    cMsg: \"Hello.\"," + "    nIcon: 3," + "    cTitle: \"JavaScript Action\"" + "});"
action = PdfJavaScriptAction(script)
link4.Action = action
newPage.Annotations.Add(link4)
page.Canvas.DrawString(text, font1, PdfBrushes.get_CadetBlue(), x, y)
y = y + size.Height + 30
label = "Need Help:  "
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
text = "Go to forum to ask questions"
link2 = PdfTextWebLink()
link2.Text = text
link2.Url = "https://www.e-iceblue.com/forum/components-f5.html"
link2.Font = font1
link2.Brush = PdfBrushes.get_CadetBlue()
link2.DrawTextWebLink(page.Canvas, PointF(x, y))
y = y + font1.MeasureString(text).Height + 30
label = "Contct us:  "
page.Canvas.DrawString(label, font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString(label, format).Width
text = "Send an email"
link2 = PdfTextWebLink()
link2.Text = text
link2.Url = "mailto:support@e-iceblue.com"
link2.Font = font1
link2.Brush = PdfBrushes.get_CadetBlue()
link2.DrawTextWebLink(page.Canvas, PointF(x, y))
y = y + font1.MeasureString(text).Height + 30
#Save pdf file.
doc.SaveToFile(outputFile)
doc.Close()