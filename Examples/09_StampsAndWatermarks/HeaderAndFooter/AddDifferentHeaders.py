from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/MultipagePDF.pdf"
outputFile = "AddingDifferentHeaders_result.pdf"

#Load the Pdf from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
header1 = "Header 1"
header2 = "Header 2"
#Define style
font = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)
brush = PdfBrushes.get_Red()
rect = RectangleF(PointF(0.0,20.0),SizeF(doc.PageSettings.Size.Width,50.0))
format = PdfStringFormat()
format.Alignment= PdfTextAlignment.Center
doc.Pages[0].Canvas.DrawString(header1,font,brush,rect,format)
font = PdfTrueTypeFont("Aleo", 15.0, PdfFontStyle.Regular,True)
brush = PdfBrushes.get_Black()
format.Alignment = PdfTextAlignment.Left
doc.Pages[1].Canvas.DrawString(header2, font, brush, rect, format)
#Save the document
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()


