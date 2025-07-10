from spire.pdf.common import *
from spire.pdf import *

def ReadFromTxt(fname: str) -> str:
    with open(fname, 'r') as f:
        text = f.read()
    return text

outputFile = "TextToPdf.pdf"
inputFile = "./Demos/Data/TextToPdf.txt"

# Get text from .txt file
text = ReadFromTxt(inputFile)
# Create a pdf document
doc = PdfDocument()
section = doc.Sections.Add()
page = section.Pages.Add()
# Create a PdfFont
font = PdfFont(PdfFontFamily.Helvetica, 11.0)
# Set string format
strformat = PdfStringFormat()
strformat.LineSpacing = 20.0
brush = PdfBrushes.get_Black()
# Set text layout
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(10.0, 20.0), page.Canvas.ClientSize)
textWidget = PdfTextWidget(text, font, brush)
textWidget.StringFormat = strformat
textWidget.Draw(page, bounds, textLayout)
# Save to file
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
