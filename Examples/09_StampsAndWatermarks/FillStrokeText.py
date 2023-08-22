from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "FillStrokeText.pdf"

#Create a pdf document and load file from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Define Pdf pen
pen = PdfPen(PdfRGBColor(Color.get_Gray()))
#Save graphics state
state = page.Canvas.Save()
#Rotate page canvas
page.Canvas.RotateTransform(-20.0)
format = PdfStringFormat()
format.CharacterSpacing = 5.0
#Draw the string on page
page.Canvas.DrawString("E-ICEBLUE", PdfFont(PdfFontFamily.Helvetica, 45.0), pen, 0.0, 500.0,format)
#Restore graphics
page.Canvas.Restore(state)
#Save the Pdf file
doc.SaveToFile(outputFile)
doc.Close()