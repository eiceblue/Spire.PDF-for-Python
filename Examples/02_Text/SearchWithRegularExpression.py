from spire.pdf.common import *
from spire.pdf import *

inputFile ="./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "ReplaceTextWithRegularExpression_out.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Create PdfTextFindCollection object to find all the phrases matching the regular expression
collection = page.FindText("\\d{4}",TextFindParameter.Regex)
newText = "New Year"
# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))
# Defines a font
font = PdfTrueTypeFont("Arial", 7.0, PdfFontStyle.Bold,True)
# Defines text horizontal/vertical center format
centerAlign = PdfStringFormat(PdfTextAlignment.Center,PdfVerticalAlignment.Middle)
for find in collection.Finds:
    # Gets the bound of the found text in page
    rec = find.Bounds
    page.Canvas.DrawRectangle(PdfBrushes.get_GreenYellow() , rec)
    # Draws new text as defined font and color
    page.Canvas.DrawString(newText, font, brush, rec,centerAlign)
    # This method can directly replace old text with newText,but it just can set the background color, can not set font/forecolor
    # find.ApplyRecoverString(newText, Color.get_Gray())
#Save the document
doc.SaveToFile(outputFile)
doc.Close()