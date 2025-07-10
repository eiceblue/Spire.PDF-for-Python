from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToPCL.pcl"
inputFile = "./Demos/Data/ToPCL.pdf"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to PCL file.
doc.SaveToFile(outputFile, FileFormat.PCL)
doc.Close()
