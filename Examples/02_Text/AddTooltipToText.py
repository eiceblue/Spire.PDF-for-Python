from spire.pdf.common import *
from spire.pdf import *

outputFile= "AddTooltipToText-result.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()
page.Canvas.DrawString("Move the mouse cursor over the following text to display a tooltip", PdfTrueTypeFont("Arial", 15.0,PdfFontStyle.Regular, True), PdfBrushes.get_Black(), PointF(10.0, 20.0))
#Define the text and its style
text1 = "Your Office Development Master"
font1 = PdfTrueTypeFont("Arial",18.0,PdfFontStyle.Regular,True)
sizeF1 = font1.MeasureString(text1)
rec1 = RectangleF(PointF(100.0,100.0), sizeF1)
#Draw text 
page.Canvas.DrawString(text1, font1, PdfSolidBrush(PdfRGBColor(Color.get_Blue())), rec1)
#Create invisible button on text position
field1 = PdfButtonField(page, "field1")
#Set the bounds and size of field
field1.Bounds = rec1
#Set tooltip content
field1.ToolTip = "E-iceblue Co. Ltd., a vendor of .NET, Java, C++ and Python development components"
#Set no border for field
field1.BorderWidth = 0.0
#Set backcolor and forcolor for field
field1.BackColor = PdfRGBColor(Color.get_Transparent())
field1.ForeColor = PdfRGBColor(Color.get_Transparent())
field1.LayoutMode = PdfButtonLayoutMode.IconOnly
field1.IconLayout.IsFitBounds = True
#Define the text and its style 
text2 = "Spire.PDF"
font2 = PdfFont(PdfFontFamily.TimesRoman, 20.0)
sizeF2 = font2.MeasureString(text2)
rec2 = RectangleF(PointF(100.0, 160.0), sizeF2)
#Draw text 
page.Canvas.DrawString(text2, font2, PdfBrushes.get_DarkOrange(), rec2)
#Create invisible button on text position
field2 = PdfButtonField(page, "field2")
field2.Bounds = rec2
field2.ToolTip = "A professional PDF library applied to creating," + "writing, editing, handling and reading PDF files" + "without any external dependencies within python application."
field2.BorderWidth = 0.0
field2.BackColor = PdfRGBColor(Color.get_Transparent())
field2.ForeColor = PdfRGBColor(Color.get_Transparent())
field2.LayoutMode = PdfButtonLayoutMode.IconOnly
field2.IconLayout.IsFitBounds = True
#Add the buttons to pdf form
doc.AllowCreateForm = True
doc.Form.Fields.Add(field1)
doc.Form.Fields.Add(field2)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()