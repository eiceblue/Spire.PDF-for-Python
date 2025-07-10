from spire.pdf.common import *
from spire.pdf import *

outputFile = "RotateNewPDF.pdf"

# Create a pdf document
doc = PdfDocument()
# Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
# Setting for page margin
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    2.0, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create PdfSection
section = doc.Sections.Add()
# Set "A4" for Pdf page
section.PageSettings.Size = PdfPageSize.A4()
# Set page margin
section.PageSettings.Margins = margin
# Set rotating angle
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle90
# Add the page
page = section.Pages.Add()
# Define a PdfBrush
brush = PdfBrushes.get_Black()
# Define a font
font = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Bold, True)
# Set the string format
format = PdfStringFormat(PdfTextAlignment.Left)
# Set the position for drawing
x = 0.0
y = 50.0
# Text string
specification = "The sample demonstrates how to rotate page when creating a PDF document."
# Draw text string on page canvas
page.Canvas.DrawString(specification, font, brush, x, y, format)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
