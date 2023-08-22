from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ImageWaterMark.pdf"
inputFile_img = "./Demos/Data/E-logo.png"
outputFile = "ImageWatermarkSecond.pdf"

#Load Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Insert an image into the first PDF page at specific position
pdfImage = PdfImage.FromFile(inputFile_img)
page = doc.Pages[0]
position = PointF(160.0, 260.0)
page.Canvas.Save()
page.Canvas.SetTransparency(0.5, 0.5, PdfBlendMode.Multiply)
page.Canvas.DrawImage(pdfImage, position)
page.Canvas.Restore()
#Save the Pdf document
doc.SaveToFile(outputFile,FileFormat.PDF)
doc.Close()