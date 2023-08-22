from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/MergePdfsTemplate_1.pdf"
inputFile2 = "./Demos/Data/MergePdfsTemplate_2.pdf"
inputFile3 = "./Demos/Data/MergePdfsTemplate_3.pdf"
outputFile = Stream("MergeFilesByStream.pdf")

#Pdf document streams 
stream1 = Stream(inputFile1)
stream2 = Stream(inputFile2)
stream3 = Stream(inputFile3)
#Pdf document streams 
streams = [stream1, stream2, stream3]
mergeOp = MergerOptions()
PdfMerger.MergeByStream(streams,outputFile,mergeOp)
