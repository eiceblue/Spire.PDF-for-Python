from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/AddTooltipForFormField.pdf"
outputFile = "AddTooltipForFormField_out.pdf"

# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Get the first page
page = doc.Pages[0]
# As for existing pdf, the property needs to be set as true
doc.AllowCreateForm = True
# Create a new pdf font
font = PdfFont(PdfFontFamily.Helvetica, 12.0, PdfFontStyle.Bold)
# Create a pdf brush
brush = PdfBrushes.get_Black()
x = 50.0
y = 590.0
tempX = 0
text = "E-mail: "
# Draw a text into page
page.Canvas.DrawString(text, font, brush, x, y)
tempX = font.MeasureString(text).Width + x + 15
# Create a pdf textbox field
textbox = PdfTextBoxField(page, "TextBox")
# Set the bounds of textbox field
textbox.Bounds = RectangleF(tempX, y, 100.0, 15.0)
# Set the border width of textbox field
textbox.BorderWidth = 0.75
# Set the border style of textbox field
textbox.BorderStyle = PdfBorderStyle.Solid
# Add the textbox field into pdf document
doc.Form.Fields.Add(textbox)
# Add a tooltip for the textbox field
doc.Form.Fields.get_Item("TextBox").ToolTip = "Please insert a valid email address"
# Save pdf document
doc.SaveToFile(outputFile)
doc.Close()
