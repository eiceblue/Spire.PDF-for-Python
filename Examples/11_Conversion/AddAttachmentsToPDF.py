from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/SampleB_2.pdf"
inputFileImg = "./Demos/Data/E-logo.png"
inputFile2 = "./Demos/Data/Sample.pdf"
outputFile = "AddAttachmentsToPDF.pdf"

# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile1)
# Load files and add in attachments
data = Stream(inputFileImg)
attach1 = PdfAttachment("attachment1.png", data)
data2 = Stream(inputFile2)
attach2 = PdfAttachment("attachment2.pdf", data2)
doc.Attachments.Add(attach1)
doc.Attachments.Add(attach2)
doc.SaveToFile(outputFile,FileFormat.PDF)
doc.Close()
