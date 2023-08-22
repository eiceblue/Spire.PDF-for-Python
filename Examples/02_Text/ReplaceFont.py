from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ReplaceFont.pdf"
outputFile = "ReplaceFont.pdf"

#Load the document from disk 
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the fonts used in PDF
fonts = doc.UsedFonts
#Create a new font 
newfont = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Regular ,True)
for font in fonts:
    #Replace the font with new font
    font.Replace(newfont)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()