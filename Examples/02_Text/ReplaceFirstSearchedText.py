from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "ReplaceFirstSearchedText_out.pdf"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Searches "Spire.PDF for .NET" by ignoring case
collection = page.FindText("Spire.PDF for Python",TextFindParameter.IgnoreCase)
newText = "Spire.PDF API"
# Gets the first found object
find = collection.Finds[0]
# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))
# Defines a font
font = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold,True)
# Gets the bound of the first found text in page
rec = find.Bounds
page.Canvas.DrawRectangle(PdfBrushes.get_White(), rec)
# Draws new text as defined font and color
page.Canvas.DrawString(newText, font, brush, rec)
# This method can directly replace old text with newText,but it just can set the background color, can not set font/forecolor
# find.ApplyRecoverString(newText, Color.get_Gray())       
#Save the document
doc.SaveToFile(outputFile)
doc.Close()