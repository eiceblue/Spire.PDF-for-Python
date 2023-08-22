from spire.pdf.common import *
from spire.pdf import *

outputFile = "AutomaticField.pdf"

def DrawAutomaticFieldP(page):
    y = 20.0

    #Title
    brush1 = PdfBrushes.get_CadetBlue()
    font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
    format1 = PdfStringFormat(PdfTextAlignment.Center)
    page.Canvas.DrawString("Automatic Field List", font1, brush1, page.Canvas.ClientSize.Width / float(2), y, format1)
    y = y + font1.MeasureString("Automatic Field List", format1).Height
    y = y + 15
    fieldList = ["DateTimeField", "CreationDateField", "DocumentAuthorField", "SectionNumberField", "SectionPageNumberField", "SectionPageCountField", "PageNumberField", "PageCountField", "DestinationPageNumberField", "CompositeField"]
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular ,True)
    fieldNameFormat = PdfStringFormat()
    fieldNameFormat.MeasureTrailingSpaces = True
    for fieldName in fieldList:
        #Draw field name
        text = "{0:s}: ".format(fieldName)
        page.Canvas.DrawString(text, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
        x = font.MeasureString(text, fieldNameFormat).Width
        bounds = RectangleF(x, y, 200.0, font.Height)
        DrawAutomaticField(fieldName, page, bounds)
        y = y + font.Height + 8

def DrawAutomaticField(fieldName, page, bounds):
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Italic,True)
    brush = PdfBrushes.get_OrangeRed()
    format = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    if "DateTimeField" == fieldName:
        field = PdfDateTimeField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.DateFormatString = "yyyy-MM-dd HH:mm:ss"
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "CreationDateField" == fieldName:
        field = PdfCreationDateField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.DateFormatString = "yyyy-MM-dd HH:mm:ss"
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "DocumentAuthorField" == fieldName:
        field = PdfDocumentAuthorField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionNumberField" == fieldName:
        field = PdfSectionNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionPageNumberField" == fieldName:
        field = PdfSectionPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionPageCountField" == fieldName:
        field = PdfSectionPageCountField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "PageNumberField" == fieldName:
        field = PdfPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "PageCountField" == fieldName:
        field = PdfPageCountField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "DestinationPageNumberField" == fieldName:
        field = PdfDestinationPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.Page = page if isinstance(page, PdfNewPage) else None
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "CompositeField" == fieldName:
        field1 = PdfSectionPageNumberField()
        field1.NumberStyle = PdfNumberStyle.LowerRoman
        field2 = PdfSectionPageCountField()
        fields = PdfCompositeField()
        fields.Font = font
        fields.Brush = brush
        fields.StringFormat = format
        fields.Bounds = bounds
        fields.AutomaticFields = [field1, field2]
        fields.Text = "section page {0} of {1}"
        graWidget = PdfGraphicsWidget(fields)
        graWidget.Draw(page.Canvas)

# Create a pdf document
doc = PdfDocument()
doc.DocumentInformation.Author = "Spire.Pdf"
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create section
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
# Create one page
page = section.Pages.Add()
# Draw automatic fields
DrawAutomaticFieldP(page)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()


