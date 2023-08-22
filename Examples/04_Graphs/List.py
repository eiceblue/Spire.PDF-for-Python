from spire.pdf.common import *
from spire.pdf import *

outputFile = "List.pdf"

#Create a pdf document
doc = PdfDocument()
#Margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
y = 10.0
#Title
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
format1 = PdfStringFormat(PdfTextAlignment.Center)
page.Canvas.DrawString("Categories List", font1, brush1,page.Canvas.ClientSize.Width / float(2), y, format1)
y = y + font1.MeasureString("Categories List", format1).Height
y = y + 5
rctg = RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize)
brush = PdfLinearGradientBrush(rctg, PdfRGBColor(Color.get_Navy()),PdfRGBColor(Color.get_OrangeRed()), PdfLinearGradientMode.Vertical)
font = PdfFont(PdfFontFamily.Helvetica, 12.0, PdfFontStyle.Bold)
formatted = "Beverages\nCondiments\nConfections\nDairy Products\nGrains/Cereals\nMeat/Poultry\nProduce\nSeafood"
#Create a list
plist = PdfList(formatted)
plist.Font = font
plist.Indent = 8
plist.TextIndent = 5
plist.Brush = brush
#Draw the list on the page
result = PdfLayoutWidget(plist).Draw(page, 0.0, y)
y = result.Bounds.Bottom
#Create another list
sortedList = PdfSortedList(formatted)
sortedList.Font = font
sortedList.Indent = 8
sortedList.TextIndent = 5
sortedList.Brush = brush
#Draw the list on the page
result2 = PdfLayoutWidget(sortedList).Draw(page, 0.0, y)
y = result2.Bounds.Bottom
marker1 = PdfOrderedMarker(PdfNumberStyle.LowerRoman, PdfFont(PdfFontFamily.Helvetica, 12.0))
list2 = PdfSortedList(formatted)
list2.Font = font
list2.Marker = marker1
list2.Indent = 8.0
list2.TextIndent = 5.0
list2.Brush = brush
result3 = PdfLayoutWidget(list2).Draw(page, 0.0, y)
y = result3.Bounds.Bottom
marker2 = PdfOrderedMarker(PdfNumberStyle.LowerLatin, PdfFont(PdfFontFamily.Helvetica, 12.0))
list3 = PdfSortedList(formatted)
list3.Font = font
list3.Marker = marker2
list3.Indent = 8.0
list3.TextIndent = 5.0
list3.Brush = brush
PdfLayoutWidget(list3).Draw(page, 0.0, y)
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()