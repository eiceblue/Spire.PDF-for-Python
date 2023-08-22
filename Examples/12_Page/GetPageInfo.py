from spire.pdf.common import *
from spire.pdf import *

def AppendAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s + "\n")
    fp.close()

outputFile = "GetPageInfo.txt"
inputFile = "./Demos/Data/GetPageInfo.pdf"

# Create a pdf document
doc = PdfDocument()
# Load an existing pdf from disk
doc.LoadFromFile(inputFile)
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the size of page MediaBox based on "point"
MediaBoxWidth = page.MediaBox.Width
MediaBoxHeight = page.MediaBox.Height
MediaBoxX = page.MediaBox.X
MediaBoxY = page.MediaBox.Y
# Get the size of page BleedBox based on "point"
BleedBoxWidth = page.BleedBox.Width
BleedBoxHeight = page.BleedBox.Height
BleedBoxX = page.BleedBox.X
BleedBoxY = page.BleedBox.Y
# Get the size of page CropBox based on "point"
CropBoxWidth = page.CropBox.Width
CropBoxHeight = page.CropBox.Height
CropBoxX = page.CropBox.X
CropBoxY = page.CropBox.Y
# Get the size of page ArtBox based on "point"
ArtBoxWidth = page.ArtBox.Width
ArtBoxHeight = page.ArtBox.Height
ArtBoxX = page.ArtBox.X
ArtBoxY = page.ArtBox.Y
# Get the size of page TrimBox based on "point"
TrimBoxWidth = page.TrimBox.Width
TrimBoxHeight = page.TrimBox.Height
TrimBoxX = page.TrimBox.X
TrimBoxY = page.TrimBox.Y
# Get the actual size of page
actualSizeW = page.ActualSize.Width
actualSizeH = page.ActualSize.Height
# Gets the rotation angle of the current page
rotationAngle = page.Rotation
rotation = str(rotationAngle)
# Create StringBuilder to save
content = []
# Add page information string to StringBuilder
content.append("MediaBox width: " + str(MediaBoxWidth) + "pt, height: " + str(MediaBoxHeight) +
               "pt, RectangleF X: " + str(MediaBoxX) + "pt, RectangleF Y: " + str(MediaBoxY) + "pt.")
content.append("BleedBox width: " + str(BleedBoxWidth) + "pt,  height: " + str(BleedBoxHeight) +
               "pt, RectangleF X: " + str(BleedBoxX) + "pt, RectangleF Y: " + str(BleedBoxY) + "pt.")
content.append("CropBox width: " + str(CropBoxWidth) + "pt,  height: " + str(CropBoxHeight) +
               "pt, RectangleF X: " + str(CropBoxX) + "pt, RectangleF Y: " + str(CropBoxY) + "pt.")
content.append("ArtBox width: " + str(ArtBoxWidth) + "pt,  height: " + str(ArtBoxHeight) +
               "pt, RectangleF X: " + str(ArtBoxX) + "pt, RectangleF Y: " + str(ArtBoxY) + "pt.")
content.append("TrimBox width: " + str(TrimBoxWidth) + "pt,  height: " + str(TrimBoxHeight) +
               "pt, RectangleF X: " + str(TrimBoxX) + "pt, RectangleF Y: " + str(TrimBoxY) + "pt.")
content.append(
    "The actual size of the current page width: " + str(actualSizeW))
content.append(
    "The actual size of the current page height: " + str(actualSizeH))
content.append("The rotation angle of the current page: " + rotation)
# Save them to a txt file
AppendAllText(outputFile, content)
doc.Close()
