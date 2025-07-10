from spire.pdf.common import *
from spire.pdf import *

outputFile = "CreateTwoColumnPDF.pdf"

# Creates a pdf document
doc = PdfDocument()
# Creates a new page
page = doc.Pages.Add()
s1 = "Spire.PDF for .NET is a professional PDF component applied to creating, writing, " + "editing, handling and reading PDF files without any external dependencies within " + ".NET application. Using this .NET PDF library, you can implement rich capabilities " + "to create PDF files from scratch or process existing PDF documents entirely through " + "C#/VB.NET without installing Adobe Acrobat."
s2 = "Many rich features can be supported by the .NET PDF API, such as security setting " + "(including digital signature), PDF text/attachment/image extract, PDF merge/split " + ", metadata update, section, graph/image drawing and inserting, table creation and " + "processing, and importing data etc.Besides, Spire.PDF for .NET can be applied to easily " + "converting Text, Image and HTML to PDF with C#/VB.NET in high quality."
# Get width and height of page
pageWidth = page.GetClientSize().Width
pageHeight = page.GetClientSize().Height
brush = PdfBrushes.get_Black()
font = PdfFont(PdfFontFamily.TimesRoman, 12.0)
format = PdfStringFormat(PdfTextAlignment.Justify)
# Draw text
page.Canvas.DrawString(s1, font, brush, RectangleF(0.0, 20.0, pageWidth / 2 - 8, pageHeight), format)
page.Canvas.DrawString(s2, font, brush, RectangleF(pageWidth / 2 + 8, 20.0, pageWidth / 2 - 8, pageHeight), format)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()