from spire.pdf.common import *
from spire.pdf import *

inputfile1 = "./Demos/Data/Overlay1.pdf"
inputfile2 = "./Demos/Data/Overlay2.pdf"
outputFile = "Overlay.pdf"

#Load two documents from disk
doc1 = PdfDocument()
doc1.LoadFromFile(inputfile1)
doc2 = PdfDocument()
doc2.LoadFromFile(inputfile2)
#Create page template
template = doc1.Pages[0].CreateTemplate()
for i in range(doc2.Pages.Count):
    page = doc2.Pages.get_Item(i)
    page.Canvas.SetTransparency(0.25,0.25, PdfBlendMode.Overlay)
    page.Canvas.DrawTemplate(template, PointF.Empty())
#Save the document
doc2.SaveToFile(outputFile)
doc1.Close()
doc2.Close()
