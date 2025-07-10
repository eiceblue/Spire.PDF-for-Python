from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SamplePDFA.pdf"
outputFile = "PDFAToPdf-result.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Create a new pdf and draw content on new file
newDoc = PdfNewDocument()
newDoc.CompressionLevel = PdfCompressionLevel.none
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    size = page.Size
    p = newDoc.Pages.Add(size, PdfMargins(0.0))
    page.CreateTemplate().Draw(p, 0.0, 0.0)    
#save file   
fileStream = Stream(outputFile)
newDoc.Save(fileStream)
fileStream.Close()
newDoc.Close(True)