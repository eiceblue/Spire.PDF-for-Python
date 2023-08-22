from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SampleB_3.pdf"
outputFile = "RearrangePageOrder.pdf"

#Create a pdf document
doc = PdfDocument()
#Load from file
doc.LoadFromFile(inputFile)
#Rearrange the page order
doc.Pages.ReArrange([1, 0])
#Save to file
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()

