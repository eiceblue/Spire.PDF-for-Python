from spire.pdf.common import *
from spire.pdf import *

inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "ReplaceTextWithRegularExpression_out.pdf"

# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the phrases matching the regular expression
finds =PdfTextFinder(doc.Pages[0])
finds.Options.Parameter =TextFindParameter.Regex
collection = finds.Find("\\d{4}")

newText = "New Year"

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 7.0, PdfFontStyle.Bold, True)
# Defines text horizontal/vertical center format
centerAlign = PdfStringFormat(
    PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

for find in collection:
    # Gets the bound of the found text in page
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)

    page.Canvas.DrawRectangle(PdfBrushes.get_GreenYellow(), rec)
    # Draws new text as defined font and color
    page.Canvas.DrawString(newText, font, brush, rec, centerAlign)

#Save the document
doc.SaveToFile(outputFile)
doc.Close()  


