from spire.pdf.common import *
from spire.pdf import *

doc =  PdfDocument()
#Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
section = doc.Sections.Add()
section.PageSettings.Margins = margin
section.PageSettings.Size = PdfPageSize.A4()
#Create one page
page = section.Pages.Add()
y = 10.0
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
format1 = PdfStringFormat(PdfTextAlignment.Center);
page.Canvas.DrawString("Spire Pdf For Python BookMark Demo", font1, brush1, page.Canvas.ClientSize.Width / float(2), y, format1)
y = y + font1.MeasureString("Spire Pdf For Python BookMark Demo", format1).Height
y = y + 5
font2 = PdfTrueTypeFont("Arial", 11.0, PdfFontStyle.Bold, True)
font3 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Bold, True)
vendors = [["First Parent BookMark", "Spire","Demo BookMark","Spire Pdf","Spire Pdf For Python"],["Second Parent BookMark" ],["Third Parent BookMark", "First Child BookMark","Second Child BookMark","Third Child BookMark","Fourth Child BookMark"]]
for i in range(len(vendors)):
    if i > 0:
        #Next page
        page = section.Pages.Add()
        y = 0.0
    #Draw vendor
    vendorTitle = "{0:d}. {1:s}".format(i + 1, vendors[i][0])
    #drawVendorLayoutResult = self._DrawVendor(page, vendors, i, vendorTitle, y)
    font1 =  PdfTrueTypeFont("Arial", 11.0, PdfFontStyle.Bold, True);
    page.Canvas.DrawString(vendorTitle, font1, PdfBrushes.get_Blue(), 0.0, y);
    #Add vendor bookmark
    vendorBookmarkDest = PdfDestination(page, PointF(0.0, y))
    vendorBookmark = doc.Bookmarks.Add(vendorTitle)
    vendorBookmark.Color = PdfRGBColor(Color.get_SaddleBrown())
    vendorBookmark.DisplayStyle = PdfTextStyle.Bold
    vendorBookmark.Action = PdfGoToAction(vendorBookmarkDest)
    vendorBookmarkColletion = PdfBookmarkCollection(vendorBookmark)
    y = y + font1.MeasureString(vendorTitle).Height + 1
    #Get parts of vendor
    for j in range(1,len(vendors[i])):
        if j > 1:
            #Next page
            page = section.Pages.Add()
            y = 0.0
        #Draw part
        partTitle = "{0:d}.{1:d}. {2:s}".format(i + 1, j, vendors[i][j])
        font1 = PdfTrueTypeFont("Arial", 11.0, PdfFontStyle.Bold, True)
        page.Canvas.DrawString(partTitle, font1, PdfBrushes.get_Brown(), 0.0, y)
        #Add part bookmark
        partBookmarkDest = PdfDestination(page, PointF(0.0, y))        
        partBookmark = vendorBookmarkColletion.Add(partTitle)
        partBookmark.Color = PdfRGBColor(Color.get_Coral())
        partBookmark.DisplayStyle = PdfTextStyle.Italic
        partBookmark.Action = PdfGoToAction(partBookmarkDest)
#Save pdf file
outputFile = "Bookmark.pdf"
doc.SaveToFile(outputFile)
doc.Close()

