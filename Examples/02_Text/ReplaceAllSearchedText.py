from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "ReplaceAllSearchedText_out.pdf"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Searches "Spire.PDF for Python" by ignoring case
finds =PdfTextFinder(doc.Pages[0])
finds.Options.Parameter =TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")
newText = "E-iceblue Spire.PDF"

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)

# rec = RectangleF()
for find in collection:
    # Gets the bound of the found text in page
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)

    page.Canvas.DrawRectangle(PdfBrushes.get_White(), rec)
    # Draws new text as defined font and color
    page.Canvas.DrawString(newText, font, brush, rec)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()
      

