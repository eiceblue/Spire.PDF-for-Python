from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/FindAndHighlightText.pdf"
outputFile = "FindAndHighlightText_out.pdf"

#Load the document from disk
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
result = None
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    result = page.FindText("science",TextFindParameter.none).Finds
    for find in result:
        #Highlight searched text
        find.ApplyHighLight()
#Save the document
pdf.SaveToFile(outputFile, FileFormat.PDF)
pdf.Close()