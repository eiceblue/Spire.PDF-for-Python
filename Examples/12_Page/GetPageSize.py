from spire.pdf.common import *
from spire.pdf import *

def AppendAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s + "\n")
    fp.close()

outputFile = "GetPageSize.txt"
inputFile = "./Demos/Data/Sample.pdf"

# Create a pdf document
doc = PdfDocument()
# Load an existing pdf from disk
doc.LoadFromFile(inputFile)
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the width of page based on "point"
pointWidth = page.Size.Width
# Get the height of page
pointHeight = page.Size.Height
# Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
# Convert the size with "pixel"
pixelWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Pixel)
pixelHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Pixel)
# Convert the size with "inch"
inchWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Inch)
inchHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Inch)
# Convert the size with "centimeter"
centimeterWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Centimeter)
centimeterHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Centimeter)
# Create StringBuilder to save
content = []
# Add pointSize string to StringBuilder
content.append("The page size of the file is (width: " +
               str(pointWidth) + "pt, height: " + str(pointHeight) + "pt).")
content.append("The page size of the file is (width: " +
               str(pixelWidth) + "pixel, height: " + str(pixelHeight) + "pixel).")
content.append("The page size of the file is (width: " +
               str(inchWidth) + "inch, height: " + str(inchHeight) + "inch).")
content.append("The page size of the file is (width: " +
               str(centimeterWidth) + "cm, height: " + str(centimeterHeight) + "cm.)")
# Save them to a txt file
AppendAllText(outputFile, content)
doc.Close()
