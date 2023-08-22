from spire.pdf.common import *
from spire.pdf import *

outputFile= "AddTransparentText-result.pdf"

doc = PdfDocument()
#Create one A4 page
page = doc.Pages.Add(PdfPageSize.A4(),PdfMargins(0.0))
page.Canvas.Save()
#Set alpha value
alpha = 0.25
page.Canvas.SetTransparency(alpha, alpha, PdfBlendMode.Normal)
#Create rectangle with specified dimensions      
rect = RectangleF(50.0, 50.0, 450.0,page.Size.Height)
#Create transparent text
text = "Spire.PDF for Python is a professional PDF development component that enables developers to"+ " create, read, edit, convert, and save PDF files in Python programs"+ " without depending on any external applications or libraries."
text += "\n\n\n\n\n"
text += "Spire.PDF for Python supports various PDF processing features including"+ "security settings, extracting text/image from PDF, merging/splitting PDF, drawing text/image/shape/barcode to PDF, etc."+ "in python applications without using Adobe Acrobat."
#Create brush from color channel
brush = PdfSolidBrush(PdfRGBColor(Color.FromArgb(30, 0, 255, 0)))
#Draw the text
page.Canvas.DrawString(text, PdfFont(PdfFontFamily.Helvetica, 14.0), brush, rect)
page.Canvas.Restore()
#Save the document
doc.SaveToFile(outputFile)
doc.Close()