from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "GoToAction_out.pdf"

def EmbeddedGoToAction(pdf, page,newPage):
    #add a attachment
    attachment = PdfAttachment(inputFile)
    pdf.Attachments.Add(attachment)
    text = "Test embedded go-to action! Click this will open the attached PDF in a new window."
    font = PdfTrueTypeFont("Arial", 13.0,PdfFontStyle.Regular,True)
    width = 490.0
    height = font.Height * 2.2
    rect = RectangleF(0.0, 100.0, width, height)
    page.Canvas.DrawString(text, font, PdfBrushes.get_Black(), rect)
    #create a PdfDestination with specific page, location and 200% zoom factor
    dest = PdfDestination(1, PointF(0.0, 842.0), 2.0)
    #create GoToE action with dest
    action = PdfEmbeddedGoToAction(attachment.FileName, dest, True)
    annotation = PdfActionAnnotation(rect, action)
    #add the annotation
    newPage.Annotations.Add(annotation)

def JumpToSpecificLocationAction(pdf, page,newPage):
    #add a new page
    pagetwo = pdf.Pages.Add()
    #draw text on the page
    pagetwo.Canvas.DrawString("This is Page Two.", PdfFont(PdfFontFamily.Helvetica, 20.0), PdfSolidBrush(PdfRGBColor(Color.get_Black())), 10.0, 10.0)
    #create PdfDestination instance and link to PdfGoToAction
    pageBottomDest = PdfDestination(pagetwo)
    pageBottomDest.Location = PointF(0.0, 5.0)
    pageBottomDest.Mode = PdfDestinationMode.Location
    pageBottomDest.Zoom = 1.0
    action = PdfGoToAction(pageBottomDest)
    buttonFont = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Bold,True)
    buttonWidth = 70.0
    buttonHeight = buttonFont.Height * 1.5
    format2 = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    buttonBounds = RectangleF(0.0, 200.0, buttonWidth, buttonHeight)
    #create a rectangle and draw text
    page.Canvas.DrawRectangle(PdfBrushes.get_DarkGray(), buttonBounds)
    page.Canvas.DrawString("To Last Page", buttonFont, PdfBrushes.get_CadetBlue(), buttonBounds, format2)
    #add the annotation
    annotation = PdfActionAnnotation(buttonBounds, action)
    annotation.Border = PdfAnnotationBorder(0.75)
    annotation.Color = PdfRGBColor(Color.get_LightGray())
    newPage.Annotations.Add(annotation)

#create a pdf document
pdf = PdfDocument()
page = pdf.Pages.Add()
newPage = (PdfNewPage)(page.Ptr)
#add a GoToE in pdf 
EmbeddedGoToAction(pdf, page,newPage)
#creat a action that could jump to specific location
JumpToSpecificLocationAction(pdf, page,newPage)
#save the fila
pdf.SaveToFile(outputFile)
pdf.Close()

