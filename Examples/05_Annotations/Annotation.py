
from spire.pdf.common import *
from spire.pdf import *

outputFile = "Annotation.pdf"

#Create a pdf document
doc = PdfDocument()
#Margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
#Title
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle['Bold'].value | PdfFontStyle['Italic'].value, True)
format1 = PdfStringFormat(PdfTextAlignment.Left)
y = 50.0
s = "The sample demonstrates how to add annotations in PDF document."
page.Canvas.DrawString(s, font1, brush1, 0.0, y-5, format1)
y = y + font1.MeasureString(s, format1).Height
y = y + 15
newPage = PdfNewPage(page.Ptr)

font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Document Link: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
dest = PdfDestination(page)
dest.Mode = PdfDestinationMode.Location
dest.Location = PointF(0.0, y)
dest.Zoom = 2.0
label = "Click me, Zoom 200%"
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
annotation = PdfDocumentLinkAnnotation(bounds, dest)
annotation.Color = PdfRGBColor(Color.get_Blue())
#newpage = PdfNewPage(page.Ptr)
newPage.Annotations.Add(annotation)
y = bounds.Bottom

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Launch File: "
size = font.MeasureString(prompt)
#pageBase =  PdfPageBase(page.Ptr)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """Launch Notepad.exe"""
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
annotation = PdfFileLinkAnnotation(bounds, "C:\\Windows\\Notepad.exe")
annotation.Color = PdfRGBColor(Color.get_Blue())
#newpage = PdfNewPage(page.Ptr)
newPage.Annotations.Add(annotation)
y = bounds.Bottom

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Text Markup: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """I'm a text box, not a TV"""
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawRectangle(PdfPen(PdfRGBColor(Color.get_Blue()), 0.1), bounds)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
location = PointF(bounds.Right + 16, bounds.Top - 16)
annotaionBounds = RectangleF(location, SizeF(80.0, 32.0))
annotation = PdfFreeTextAnnotation(annotaionBounds)
annotation.AnnotationIntent = PdfAnnotationIntent.FreeTextCallout
annotation.Border = PdfAnnotationBorder(0.5)
annotation.BorderColor = PdfRGBColor(Color.get_Red())
location = PointF(bounds.Right + 16, bounds.Top - 16)
annotation.CalloutLines = [PointF(bounds.Right, bounds.Top), PointF(bounds.Right+8, bounds.Top - 8), location]
annotation.Color = PdfRGBColor(Color.get_Yellow())
annotation.Flags = PdfAnnotationFlags.Locked
annotation.Font = font
annotation.LineEndingStyle = PdfLineEndingStyle.OpenArrow
annotation.MarkupText = "Just a joke."
annotation.Opacity = 0.75
annotation.TextMarkupColor =PdfRGBColor(Color.get_Green())
newPage.Annotations.Add(annotation)
y = bounds.Bottom

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Line Annotation: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """Line Anotation"""
size = font.MeasureString(label)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
bounds = RectangleF(x, y, size.Width, size.Height)
linePoints = [int(bounds.Left), int(bounds.Top), int(bounds.Right), int(bounds.Bottom)]
annotation = PdfLineAnnotation(linePoints, "Annotation")
annotation.BeginLineStyle = PdfLineEndingStyle.ClosedArrow
annotation.EndLineStyle = PdfLineEndingStyle.ClosedArrow
annotation.LineCaption = True
annotation.BackColor = PdfRGBColor(Color.get_Black())
annotation.CaptionType = PdfLineCaptionType.Inline
newPage.Annotations.Add(annotation)
y = bounds.Bottom

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Highlight incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of anotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
size = font.MeasureString("demo of ", format)
x = x + size.Width
incorrectWordLocation = PointF(x, y)
markupText = "Should be 'annotation'"
annotation = PdfTextMarkupAnnotation(markupText, "anotation",RectangleF(x, y, 100.0, 100.0), font)
annotation.TextMarkupAnnotationType = PdfTextMarkupAnnotationType.Highlight
annotation.TextMarkupColor = PdfRGBColor(Color.get_LightSkyBlue())
newPage.Annotations.Add(annotation)
y = y + size.Height

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Markup incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of annotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
x = x + font.MeasureString(label, format).Width
markupText = "All words were spelled correctly"
size = font.MeasureString(markupText)
annotation = PdfPopupAnnotation(RectangleF(PointF(x, y), SizeF.Empty()), markupText)
annotation.Icon = PdfPopupIcon.Paragraph
annotation.Open = True
annotation.Color = PdfRGBColor(Color.get_Yellow())
newPage.Annotations.Add(annotation)
y = y + size.Height

y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Markup incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of annotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
x = x + font.MeasureString(label, format).Width
markupText = "Just a draft, not checked."
size = font.MeasureString(markupText)
annotation = PdfRubberStampAnnotation(RectangleF(x, y, font.Height, font.Height), markupText)
annotation.Icon = PdfRubberStampAnnotationIcon.Draft
annotation.Color = PdfRGBColor(Color.get_Plum())
newPage.Annotations.Add(annotation)
y = y + size.Height

#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()
