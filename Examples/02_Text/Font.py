from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Font.pdf"
inputFontFile = "./Demos/Data/PT_Serif-Caption-Web-Regular.ttf"
outputFile = "Font.pdf"

#Create a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Create one page
page = doc.Pages[0]
#Draw the text
l = page.Canvas.ClientSize.Width / float(2)
center = PointF(l, l)
r = float(2 * l * l)
brush = PdfRadialGradientBrush(center, 0.0, center, r, PdfRGBColor(Color.get_Blue()),PdfRGBColor(Color.get_Red()))
y = 200
i = 0
text = "Font Family: Helvetica"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.Helvetica, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)
i += 1
text = "Font Family: Courier"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.Courier, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)
i += 1
text = "Font Family: TimesRoman"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.TimesRoman, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)
i += 1
text = "Font Family: Symbol"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.Symbol, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)
i += 1
text = "Font Family: ZapfDingbats"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.ZapfDingbats, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)
i += 1
#True type font - embedded
trueTypeFont = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold,True)
page.Canvas.DrawString("Font Family: Arial - Embedded", trueTypeFont, brush, 40.0, (y := y + 26.0))
#Right to left
arabicText = "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0628\u062F\u0648\u0631\u0647\u0020\u062D\u0648\u0644\u0647\u0627\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021"
trueTypeFont = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold,True)
rctg = RectangleF(PointF(40.0, (y := y + 26)), page.Canvas.ClientSize)
strformat = PdfStringFormat(PdfTextAlignment.Right)
strformat.RightToLeft = True
page.Canvas.DrawString(arabicText, trueTypeFont, brush, rctg, strformat)
#True type font - not embedded
trueTypeFont = PdfTrueTypeFont("Batang", 14.0, PdfFontStyle.Italic,True)
page.Canvas.DrawString("Font Family: Batang - Not Embedded", trueTypeFont, brush, 40.0, (y := y + 16.0))
#Font file
trueTypeFont = PdfTrueTypeFont(inputFontFile, 20.0)
page.Canvas.DrawString("PT Serif Caption Font", trueTypeFont, brush, 40.0, (y := y + 36.0))
page.Canvas.DrawString("PT Serif Caption Font", PdfFont(PdfFontFamily.Helvetica, 8.0), brush, 40.0, (y := y + 40.0))
#Cjk font
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.MonotypeHeiMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Chinese? \u5B57\u4F53", cjkFont, brush, 40.0, (y := y + 36.0))
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.HanyangSystemsGothicMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Japanese? \u30D5\u30A9\u30F3\u30C8", cjkFont, brush, 40.0, (y := y + 36.0))
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.HanyangSystemsShinMyeongJoMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Korean? \uAE00\uAF34", cjkFont, brush, 40.0, (y := y + 36.0))
#Save the document
doc.SaveToFile(outputFile)
doc.Close()