from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SampleB_1.pdf"
outputFile = "FindTextInDefineArea.pdf"

# Load document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Define a rectangle
rctg = RectangleF(0.0, 0.0, 300.0, 300.0)
pdfPageBase = doc.Pages.get_Item(0)
findCollection = pdfPageBase.FindText(rctg,"Spire",TextFindParameter.WholeWord)
findCollectionOut = pdfPageBase.FindText(rctg,"PDF",TextFindParameter.WholeWord)
# Find text in the rectangle
for find in findCollection.Finds:
        #Highlight searched text
        find.ApplyHighLight(Color.get_Green())
for findOut in findCollectionOut.Finds:
        #Highlight searched text
        findOut.ApplyHighLight(Color.get_Yellow())
doc.SaveToFile(outputFile,FileFormat.PDF)
doc.Close()