
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/pdfTemplate_N.pdf"
outputFile = "AddTextBoxField_out.pdf"

#Open pdf document    
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get the first page
page = pdf.Pages[0]
#As for existing pdf, the property needs to be set as true
pdf.AllowCreateForm = True
#Create a new pdf font
font = PdfFont(PdfFontFamily.Helvetica, 12.0, PdfFontStyle.Bold)
#Create a pdf brush
brush = PdfBrushes.get_Black()
x = 50.0
y = 550.0
tempX = 0
text = "TexBox: "
#Draw a text into page
page.Canvas.DrawString(text, font, brush, x, y)
#Add a textBox field
tempX = font.MeasureString(text).Width + x + 15
textbox = PdfTextBoxField(page, "TextBox")
textbox.Bounds = RectangleF(tempX, y, 100.0, 15.0)
textbox.BorderWidth = 0.75
textbox.BorderStyle = PdfBorderStyle.Solid
pdf.Form.Fields.Add(textbox)
#Save the document
pdf.SaveToFile(outputFile)
pdf.Close()
