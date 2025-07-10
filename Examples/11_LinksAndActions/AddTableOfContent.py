from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/AddTableOfContent.pdf"
outputFile = "AddTableOfContent_out.pdf"

#open a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#get the page count
pageCount = doc.Pages.Count
#insert a blank page into the pdf document
tocPage = doc.Pages.Insert(0)
#set title
title = "Table Of Contents"
titleFont = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Bold, True)
centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
location = PointF(tocPage.Canvas.ClientSize.Width / float(2), titleFont.MeasureString(title).Height)
tocPage.Canvas.DrawString(title, titleFont, PdfBrushes.get_CornflowerBlue(), location, centerAlignment)
#draw TOC text
titlesFont = PdfTrueTypeFont("Arial", 14.0,PdfFontStyle.Regular,True)
titles = [None for _ in range(pageCount)]
i = 0
while i < len(titles):
    titles[i] = "This is page{0:d}".format(i+1)
    i += 1
y = titleFont.MeasureString(title).Height + 10
x = 0.0
newPage = PdfNewPage(tocPage.Ptr)
for i in range(1, pageCount + 1):
    text = titles[i-1]
    titleSize = titlesFont.MeasureString(text)
    navigatedPage = doc.Pages[i]
    pageNumText = str((i+1))
    pageNumTextSize = titlesFont.MeasureString(pageNumText)
    tocPage.Canvas.DrawString(text, titlesFont, PdfBrushes.get_CadetBlue(), 0.0, y)
    dotLocation = titleSize.Width + 2 + x
    pageNumlocation = tocPage.Canvas.ClientSize.Width - pageNumTextSize.Width
    #for j in arange(dotLocation, pageNumlocation):
    while dotLocation < pageNumlocation :
        if dotLocation >= pageNumlocation:
            break
        tocPage.Canvas.DrawString(".", titlesFont, PdfBrushes.get_Gray(), dotLocation, y)
        dotLocation += 3
    tocPage.Canvas.DrawString(pageNumText, titlesFont, PdfBrushes.get_CadetBlue(), pageNumlocation, y)
    #add TOC action
    location = PointF(0.0, y)
    titleBounds = RectangleF(location, SizeF(tocPage.Canvas.ClientSize.Width, titleSize.Height))
    Dest = PdfDestination(navigatedPage, PointF(-doc.PageSettings.Margins.Top, -doc.PageSettings.Margins.Left))
    gotoAction = PdfGoToAction(Dest)
    action = PdfActionAnnotation(titleBounds, gotoAction)
    action.Border = PdfAnnotationBorder(0.0)
    #newPage = PdfNewPage(tocPage.Ptr)
    newPage.Annotations.Add(action)
    y += titleSize.Height + 10
#save pdf document
doc.SaveToFile(outputFile)