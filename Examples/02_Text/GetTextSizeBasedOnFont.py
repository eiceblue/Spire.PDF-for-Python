from spire.pdf.common import *
from spire.pdf import *


def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

outputFile = "GetTextSizeBasedOnFont.txt"

text = "Spire.PDF for Python"
# Create an instance for PdfFont
font1 = PdfFont(PdfFontFamily.TimesRoman, 12.0)
# Get text size based on font name and size
sizeF1 = font1.MeasureString(text)
stringBuilder = "1. The width is: " + str(sizeF1.Width) + ", the height is: " + str(sizeF1.Height)
# Create an instance for PdfTrueTypeFont
font2 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
# Get text size based on font name and size
sizeF2 = font2.MeasureString(text)
stringBuilder += "2. The width is: " + str(sizeF2.Width) + ", the height is: " + str(sizeF2.Height)
WriteAllText(outputFile, stringBuilder)