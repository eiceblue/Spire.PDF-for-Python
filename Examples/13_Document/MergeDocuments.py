from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/MergePdfsTemplate_1.pdf"
inputFile2 = "./Demos/Data/MergePdfsTemplate_2.pdf"
inputFile3 = "./Demos/Data/MergePdfsTemplate_3.pdf"
outputFile = "MergeDocuments.pdf"

#Pdf document list
files = [inputFile1, inputFile2, inputFile3]
#Open pdf documents            
docs = [None for _ in range(len(files))]
i = 0
while i < len(files):
    docs[i] = PdfDocument()
    docs[i].LoadFromFile(files[i])
    i += 1
#Append document
docs[0].AppendPage(docs[1])
#Import page
for i in range(0, docs[2].Pages.Count, 2):
    docs[0].InsertPage(docs[2], i)
#Save pdf file
docs[0].SaveToFile(outputFile)
#Close
for doc in docs:
    doc.Close()
