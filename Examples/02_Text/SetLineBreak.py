from spire.pdf.common import *
from spire.pdf import *

outputFile = "SetLineBreak_out.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one A4 page
page = doc.Pages.Add(PdfPageSize.A4(), PdfMargins(40.0))
#Create brush from color channel
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
#Create text
text = "Spire.PDF for Python" + "\n" + "A professional PDF library applied to" + " creating, writing, editing, handling and reading PDF files" + " without any external dependencies within python application."
text += "\n\rSpire.PDF for Java" + "\n" + "A PDF Java API that enables developers to read, " + "write, convert and print PDF documents" + "in Java applications without using Adobe Acrobat."
text += "\n\r"
text += "Welcome to evaluate Spire.PDF!"
#Create rectangle with specified dimensions      
rect = RectangleF(50.0, 50.0, page.Size.Width - 150.0, page.Size.Height)
#Draw the text
page.Canvas.DrawString(text, PdfFont(PdfFontFamily.Helvetica, 13.0), brush, rect)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()