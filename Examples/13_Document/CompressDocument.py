from spire.pdf.common import *
from spire.pdf import *

outputFile = "CompressDocument.pdf"
inputFile = "./Demos/Data/CompressDocument.pdf"

#Load the pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Compress the content in document
doc.FileInfo.IncrementalUpdate = False
#Set the compression level to best
doc.CompressionLevel = PdfCompressionLevel.Best
#Disable the incremental update
doc.FileInfo.IncrementalUpdate = False
#Traverse all pages
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    if page is not None:
        if page.ImagesInfo is not None:
            for info in page.ImagesInfo:
                page.TryCompressImage(info.Index)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
