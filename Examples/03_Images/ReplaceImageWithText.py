from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/ReplaceImage.pdf"
outputFile = "ReplaceImageWithText.pdf"

#Create a pdf document
doc = PdfDocument()
#Load file from disk.
doc.LoadFromFile(inputfile)
#Get the first page.
page = doc.Pages[0]
#Get images of the first page.
# change: imageInfo = page.ImagesInfo
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
image = PdfImage.FromStream(imageInfo[0].Image)
#Get width and height of image
widthInPixel = image.Width
heightInPixel = image.Height
#Convert unit from Pixel to Point
convertor = PdfUnitConvertor()
width = convertor.ConvertFromPixels(float(widthInPixel), PdfGraphicsUnit.Point)
height = convertor.ConvertFromPixels(float(heightInPixel), PdfGraphicsUnit.Point)
#Get location of image
xPos = imageInfo[0].Bounds.X
yPos = imageInfo[0].Bounds.Y
#Remove the image
# change: page.DeleteImage(0)
imageHelper.DeleteImage(imageInfo[0])
#Define a rectangle
rect = RectangleF(PointF(xPos, yPos), SizeF(width, height))
#Define string format
strformat = PdfStringFormat()
strformat.Alignment= PdfTextAlignment.Center
strformat.LineAlignment= PdfVerticalAlignment.Middle
#Draw a string at the location of the image
page.Canvas.DrawString("ReplacedText", PdfFont(PdfFontFamily.Helvetica, 18.0), PdfBrushes.get_Purple(), rect, strformat)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()

