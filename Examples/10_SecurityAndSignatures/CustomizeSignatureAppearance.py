from spire.pdf.common import *
from spire.pdf import *

class MyPdfCustomAppearance(IPdfSignatureAppearance):
    def __init__(self):
        super(MyPdfCustomAppearance,self).__init__(None) 

    def Generate(self, g: PdfCanvas):
        x = 0.0
        y = 0.0
        fontSize = 10.0
        font = PdfTrueTypeFont("Times New Roman", fontSize, PdfFontStyle.Regular, True)
        lineHeight = fontSize
        image = PdfImage.FromFile("data/E-iceblueLogo.png")
        g.DrawImage(image, x, y)
        x = float(image.Width)
        g.DrawString("Signer: Gary", font, PdfBrushes.get_Red(), PointF(x, y))
        y += lineHeight + 5
        g.DrawString("Phone: +86 12345678", font, PdfBrushes.get_Black(), PointF(x, y))
        y += lineHeight + 5
        g.DrawString("Address: Sichuan Province, China", font, PdfBrushes.get_Black(), PointF(x, y))

inputFile = "data/SampleB_1.pdf"
inputFile_pfx = "data/gary.pfx"
outputFile = "CustomizeSignatureAppearance.pdf"

doc = PdfDocument()
doc.LoadFromFile(inputFile)
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")
my_appearance = MyPdfCustomAppearance()
callback_ptr=my_appearance.register_callback()
customAppearance= PdfCustomAppearance(callback_ptr)
signatureMaker.MakeSignature("Signer", doc.Pages.get_Item(0), 90.0, 550.0, 270.0, 640.0, customAppearance)
doc.SaveToFile(outputFile)
doc.Close()