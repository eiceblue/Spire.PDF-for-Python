from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/E-iceblueLogo.png"
outputFile = "ImageAndPageNumber_out.pdf"

def CreateHeaderTemplate( margins, pageSize):
    #create a PdfPageTemplateElement object as header space
    headerSpace = PdfPageTemplateElement(pageSize.Width, margins.Top)
    headerSpace.Foreground = False
    #declare two float variables
    x = margins.Left
    y = 0.0
    #draw image in header space 
    headerImage = PdfImage.FromFile(inputFile)
    width = headerImage.Width / float(2)
    height = headerImage.Height / float(2)
    headerSpace.Graphics.DrawImage(headerImage, x, margins.Top - height - 5, width, height)
    #draw line in header space
    pen = PdfPen(PdfBrushes.get_LightGray(), 1.0)
    headerSpace.Graphics.DrawLine(pen, x, y + margins.Top - 2, pageSize.Width - x, y + margins.Top - 2)
    #return headerSpace
    return headerSpace
def CreateFooterTemplate(margins, pageSize):
    #create a PdfPageTemplateElement object which works as footer space
    footerSpace = PdfPageTemplateElement(pageSize.Width, margins.Bottom)
    footerSpace.Foreground = False
    #declare two float variables
    x = margins.Left
    y = 0.0
    #draw line in footer space
    pen = PdfPen(PdfBrushes.get_Gray(), 1.0)
    footerSpace.Graphics.DrawLine(pen, x, y, pageSize.Width - x, y)
    #draw text in footer space
    y = y + 5
    font = PdfTrueTypeFont("Arial", 10.0,PdfFontStyle.Regular, True)
    #draw dynamic field in footer space
    number = PdfPageNumberField()
    count = PdfPageCountField()
    listAutomaticField = [number, count]
    compositeField = PdfCompositeField(font, PdfBrushes.get_Black(), "Page {0} of {1}", listAutomaticField)
    compositeField.StringFormat = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Top)
    size = font.MeasureString(compositeField.Text)
    compositeField.Bounds = RectangleF(x, y, size.Width, size.Height)
    newTemplate = compositeField
    templateGraphicsWidget = PdfGraphicsWidget(newTemplate.Ptr)
    templateGraphicsWidget.Draw(footerSpace.Graphics)
    #return footerSpace
    return footerSpace

#create a PDF document
doc = PdfDocument()
doc.PageSettings.Size = PdfPageSize.A4()
#reset the default margins to 0
doc.PageSettings.Margins = PdfMargins(0.0)
#create a PdfMargins object, the parameters indicate the page margins you want to set
margins = PdfMargins(50.0, 50.0, 50.0, 50.0)
#get page size
pageSize = doc.PageSettings.Size
#create a header template with content and apply it to page template
doc.Template.Top = CreateHeaderTemplate( margins, pageSize)
#create a footer template with content and apply it to page template
doc.Template.Bottom = CreateFooterTemplate( margins, pageSize)
#apply blank templates to other parts of page template
docSizeHeight = doc.PageSettings.Size.Height
doc.Template.Left = PdfPageTemplateElement(margins.Left, docSizeHeight)
doc.Template.Right = PdfPageTemplateElement(margins.Right, docSizeHeight)
#save the file
doc.SaveToFile(outputFile,FileFormat.PDF)
doc.Close()




