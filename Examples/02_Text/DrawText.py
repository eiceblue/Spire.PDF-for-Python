from spire.pdf.common import *
from spire.pdf import *

def DrawText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw text - brush
    text = "Go! Turn Around! Go! Go! Go!"
    pen = PdfPens.get_DeepSkyBlue()
    brush = PdfSolidBrush(PdfRGBColor(Color.get_White()))
    format = PdfStringFormat()
    font = PdfFont(PdfFontFamily.Helvetica, 18.0, PdfFontStyle.Italic)
    size = font.MeasureString(text, format)
    rctg = RectangleF(page.Canvas.ClientSize.Width / float(2) + 10, 180.0, size.Width / 3 * 2, size.Height * 2)
    page.Canvas.DrawString(text, font, pen, brush, rctg, format)
    #Restore graphics
    page.Canvas.Restore(state)

def TransformText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw the text - transform    
    font = PdfFont(PdfFontFamily.Helvetica, 18.0)
    brush1 = PdfSolidBrush(PdfRGBColor(Color.get_DeepSkyBlue()))
    brush2 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
    page.Canvas.TranslateTransform(20.0, 200.0)
    page.Canvas.ScaleTransform(1.0, 0.6)
    page.Canvas.SkewTransform(-10, 0.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush1, 0.0, 0.0)
    page.Canvas.SkewTransform(10.0, 0.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush2, 0.0, 0.0)
    page.Canvas.ScaleTransform(1.0, -1.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush2, 0.0, -2 * 18.0)
    #Restore graphics
    page.Canvas.Restore(state)

def AlignText(page):
    #Draw the text - alignment
    font = PdfFont(PdfFontFamily.Helvetica, 20.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    leftAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Left!", font, brush, 0.0, 20.0, leftAlignment)
    page.Canvas.DrawString("Left!", font, brush, 0.0, 50.0, leftAlignment)
    rightAlignment = PdfStringFormat(PdfTextAlignment.Right, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Right!", font, brush, page.Canvas.ClientSize.Width, 20.0, rightAlignment)
    page.Canvas.DrawString("Right!", font, brush, page.Canvas.ClientSize.Width, 50.0, rightAlignment)
    centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, page.Canvas.ClientSize.Width / float(2), 40.0, centerAlignment)

def AlignTextInRectangle(page):
    #Draw the text - align in rectangle
    font = PdfFont(PdfFontFamily.Helvetica, 10.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    rctg1 = RectangleF(0.0, 70.0, page.Canvas.ClientSize.Width / float(2), 100.0)
    rctg2 = RectangleF(page.Canvas.ClientSize.Width / float(2), 70.0, page.Canvas.ClientSize.Width / float(2), 100.0)
    page.Canvas.DrawRectangle(PdfSolidBrush(PdfRGBColor(Color.get_LightBlue())), rctg1)
    page.Canvas.DrawRectangle(PdfSolidBrush(PdfRGBColor(Color.get_LightSkyBlue())), rctg2)
    leftAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Top)
    page.Canvas.DrawString("Left! Left!", font, brush, rctg1, leftAlignment)
    page.Canvas.DrawString("Left! Left!", font, brush, rctg2, leftAlignment)
    rightAlignment = PdfStringFormat(PdfTextAlignment.Right, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Right! Right!", font, brush, rctg1, rightAlignment)
    page.Canvas.DrawString("Right! Right!", font, brush, rctg2, rightAlignment)
    centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Bottom)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, rctg1, centerAlignment)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, rctg2, centerAlignment)

def RotateText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw the text - transform    
    font = PdfFont(PdfFontFamily.Helvetica, 10.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    centerAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    x = page.Canvas.ClientSize.Width / float(2)
    y = 380.0
    page.Canvas.TranslateTransform(x, y)
    for i in range(0, 12):
        page.Canvas.RotateTransform(30.0)
        page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, 20.0, 0.0, centerAlignment)
    #Restore graphics
    page.Canvas.Restore(state)

outputFile = "DrawText.pdf"

#Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()
DrawText(page)
AlignText(page)
AlignTextInRectangle(page)
TransformText(page)
RotateText(page)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()







