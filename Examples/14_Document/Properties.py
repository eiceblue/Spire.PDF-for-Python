from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Properties.pdf"
outputFile = "Properties.pdf"

#Load pdf document
doc = PdfDocument()
doc.LoadFromFile( inputFile)
#Set document info
doc.DocumentInformation.Author = "E-iceblue"
doc.DocumentInformation.Creator = "E-iceblue"
doc.DocumentInformation.Keywords = "pdf, demo, document information"
doc.DocumentInformation.Producer = "Spire.Pdf"
doc.DocumentInformation.Subject = "Demo of Spire.Pdf"
doc.DocumentInformation.Title = "Document Information"
#File info
doc.FileInfo.CrossReferenceType = PdfCrossReferenceType.CrossReferenceStream
doc.FileInfo.IncrementalUpdate = False
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()
