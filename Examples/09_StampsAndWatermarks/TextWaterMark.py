from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ImageWaterMark.pdf"
outputFile = "TextWaterMark.pdf"

#Create a pdf document and load file from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Draw text watermark
brush = PdfTilingBrush(SizeF(page.Canvas.ClientSize.Width / float(2), page.Canvas.ClientSize.Height / float(3)))
brush.Graphics.SetTransparency(0.3)
brush.Graphics.Save()
brush.Graphics.TranslateTransform(brush.Size.Width / float(2), brush.Size.Height / float(2))
brush.Graphics.RotateTransform(-45.0)
brush.Graphics.DrawString("Spire.Pdf Demo", PdfFont(PdfFontFamily.Helvetica, 24.0), PdfBrushes.get_Violet(), 0.0, 0.0, PdfStringFormat(PdfTextAlignment.Center))
brush.Graphics.Restore()
brush.Graphics.SetTransparency(1.0)
page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize))
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()