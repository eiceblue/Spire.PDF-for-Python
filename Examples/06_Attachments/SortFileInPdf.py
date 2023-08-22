from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/SampleB_1.pdf"
inputFile2 = "./Demos/Data/SampleB_2.pdf"
inputFile3 = "./Demos/Data/SampleB_3.pdf"
outputFile = "SortFileInPdf.pdf"

#Create a pdf document
doc = PdfDocument()
doc.Collection.AddCustomField("No", "number", CustomFieldType.NumberField)
doc.Collection.AddFileRelatedField("Desc", "desc", FileRelatedFieldType.Desc)
doc.Collection.Sort(["No", "Desc"], [True, True])
pdfAttachment = PdfAttachment(inputFile1)
doc.Collection.AddAttachment(pdfAttachment)
pdfAttachment = PdfAttachment(inputFile2)
doc.Collection.AddAttachment(pdfAttachment)
pdfAttachment = PdfAttachment(inputFile3)
doc.Collection.AddAttachment(pdfAttachment)
i = 1
for attachment in doc.Collection.AssociatedFiles:
    attachment.SetFieldValue("No", i)
    attachment.SetFieldValue("Desc", attachment.FileName)
    i += 1
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
