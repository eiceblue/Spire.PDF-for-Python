from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/pdfTemplate_N.pdf"
outputFile = "AddTilingBackgroundImage.pdf"

#Load document from disk
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Load an image
image = PdfImage.FromFile("./Demos/Data/E-iceblueLogo.png")
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    #Create PdfTilingBrush
    brush = PdfTilingBrush(SizeF(page.Canvas.Size.Width / float(3), page.Canvas.Size.Height / float(5)))
    #Set the transparency
    brush.Graphics.SetTransparency(0.3)
    #Draw image on brush graphics
    brush.Graphics.DrawImage(image, PointF((brush.Size.Width - image.Width) / float(2), (brush.Size.Height - image.Height) / float(2)))
    #use the brush to draw rectangle
    page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.Size))
#Save the Pdf document
pdf.SaveToFile(outputFile,FileFormat.PDF)
pdf.Close()

