from spire.pdf.common import *
from spire.pdf import *

def ReadText(fname:str):
    with open(fname, 'r') as f:
      content = f.read()
      return content

inputFile1 = "./Data/PdfImage.png"
inputFile2 = "./Data/text.txt"
output = "PlaceTextAroundImage_out.pdf"

# Creates a pdf document
doc = PdfDocument()

# Creates a page 
page = doc.Pages.Add()

#Gets page width
pageWidth = page.Canvas.ClientSize.Width
y = 0.0

y = y + 8

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))

# Defines a font
font1 = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Bold ,True)

# Defines a text center alignment format
format1 = PdfStringFormat(PdfTextAlignment.Center)
format1.CharacterSpacing = 1.0

text = "Spire.PDF for Python"
# Draws text at the specified position
page.Canvas.DrawString(text, font1, brush, pageWidth / 2, y, format1)
# Get the size of text
size = font1.MeasureString(text, format1)
y = y + size.Height + 6

# Loads an image 
image = PdfImage.FromFile(inputFile1)

# Draws image at the specified position
page.Canvas.DrawImage(image, PointF(pageWidth - image.PhysicalDimension.Width, y))
imageLeftSpace = pageWidth - image.PhysicalDimension.Width - 2
imageBottom = image.PhysicalDimension.Height + y

format2 = PdfStringFormat()
# Loads the text around the image
text = ReadText(inputFile2)

font2 = PdfTrueTypeFont("Arial", 16.0 , PdfFontStyle.Regular, True)

#Set line spacing
format2.LineSpacing = font2.Size * 1.5

textLayouter = PdfStringLayouter()
imageLeftBlockHeight = imageBottom - y
# Splits the text around into multiple lines based on the draw area
result = textLayouter.Layout(text, font2, format2, SizeF(imageLeftSpace, imageLeftBlockHeight))
if result.ActualSize.Height < imageLeftBlockHeight:
    imageLeftBlockHeight = imageLeftBlockHeight + result.LineHeight
    result = textLayouter.Layout(text, font2, format2, SizeF(imageLeftSpace, imageLeftBlockHeight))
# Draws all the lines onto the page
for line in result.Lines:
    page.Canvas.DrawString(line.Text, font2, brush, 0.0, y, format2)
    y = y + result.LineHeight

# Draw the rest of the text onto the page
textWidget = PdfTextWidget(result.Remainder, font2, brush)
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
textWidget.StringFormat = format2
textWidget.Draw(page, bounds, textLayout)

#Save the document
doc.SaveToFile(output)