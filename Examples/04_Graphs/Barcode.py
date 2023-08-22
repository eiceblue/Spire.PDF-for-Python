
from spire.pdf.common import *
from spire.pdf import *

outputFile = "Barcode.pdf"

# Create a pdf document.
doc = PdfDocument()
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
section = doc.Sections.Add()
section.PageSettings.Margins = margin
section.PageSettings.Size = PdfPageSize.A4()
# Create one page
page = section.Pages.Add()
y = 10.0
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Bold, True)
rctg = RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize)
brush2 = PdfLinearGradientBrush(rctg, PdfRGBColor(Color.get_Navy()), PdfRGBColor(
    Color.get_OrangeRed()), PdfLinearGradientMode.Vertical)
# Draw Codabar
text = PdfTextWidget()
text.Font = font1
text.Text = "Codabar:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode1 = PdfCodabarBarcode("00:12-3456/7890")
barcode1.BarcodeToTextGapHeight = 1.0
barcode1.EnableCheckDigit = True
barcode1.ShowCheckDigit = True
barcode1.TextDisplayLocation = TextLocation.Bottom
barcode1.TextColor = PdfRGBColor(Color.get_Blue())
barcode1.Draw(page, PointF(0.0, y))
y = barcode1.Bounds.Bottom + 5
# Draw Code11Barcode
text.Text = "Code11:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode2 = PdfCode11Barcode("123-4567890")
barcode2.BarcodeToTextGapHeight = 1.0
barcode2.TextDisplayLocation = TextLocation.Bottom
barcode2.TextColor = PdfRGBColor(Color.get_Blue())
barcode2.Draw(page, PointF(0.0, y))
y = barcode2.Bounds.Bottom + 5
# Draw Code32
text.Text = "Code32:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode5 = PdfCode32Barcode("16273849")
barcode5.BarcodeToTextGapHeight = 1.0
barcode5.TextDisplayLocation = TextLocation.Bottom
barcode5.TextColor = PdfRGBColor(Color.get_Blue())
barcode5.Draw(page, PointF(0.0, y))
y = barcode5.Bounds.Bottom + 5
page = section.Pages.Add()
y = 10.0
# Draw Code39
text.Text = "Code39:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode6 = PdfCode39Barcode("16-273849")
barcode6.BarcodeToTextGapHeight = 1.0
barcode6.TextDisplayLocation = TextLocation.Bottom
barcode6.TextColor = PdfRGBColor(Color.get_Blue())
barcode6.Draw(page, PointF(0.0, y))
y = barcode6.Bounds.Bottom + 5
# Draw Code39-E
text.Text = "Code39-E:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode7 = PdfCode39ExtendedBarcode("16-273849")
barcode7.BarcodeToTextGapHeight = 1.0
barcode7.TextDisplayLocation = TextLocation.Bottom
barcode7.TextColor = PdfRGBColor(Color.get_Blue())
barcode7.Draw(page, PointF(0.0, y))
y = barcode7.Bounds.Bottom + 5
# Draw Code93
text.Text = "Code93:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode8 = PdfCode93Barcode("16-273849")
barcode8.BarcodeToTextGapHeight = 1.0
barcode8.TextDisplayLocation = TextLocation.Bottom
barcode8.TextColor = PdfRGBColor(Color.get_Blue())
barcode8.QuietZone.Bottom = 5.0
barcode8.Draw(page, PointF(0.0, y))
y = barcode8.Bounds.Bottom + 5
# Draw Code93-E
text.Text = "Code93-E:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode9 = PdfCode93ExtendedBarcode("16-273849")
barcode9.BarcodeToTextGapHeight = 1.0
barcode9.TextDisplayLocation = TextLocation.Bottom
barcode9.TextColor = PdfRGBColor(Color.get_Blue())
barcode9.Draw(page, PointF(0.0, y))
y = barcode9.Bounds.Bottom + 5
# Save the document
outputFile = TestUtil.OUTPUT + "Demo/Barcode.pdf"
doc.SaveToFile(outputFile)
doc.Close()