from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "ReplaceFirstSearchedText_out.pdf"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Searches "Spire.PDF for Python" by ignoring case
finds =PdfTextFinder(page)
finds.Options.Parameter =TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")
newText = "Spire.PDF API"
# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)

# Gets the bound of the first found text in page
rec = RectangleF(collection[0].Positions[0].X, collection[0].Positions[0].Y, collection[0].Sizes[0].Width, collection[0].Sizes[0].Height)

page.Canvas.DrawRectangle(PdfBrushes.get_White(), rec)

# Draws new text as defined font and color
page.Canvas.DrawString(newText, font, brush, rec)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()   

     

