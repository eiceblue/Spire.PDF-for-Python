from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToPdfA2B.pdf"
inputFile = "./Demos/Data/ToPdfA2B.pdf"

# Convert to PDFA file
converter = PdfStandardsConverter(inputFile)
# also supports ToPdfA1B ToPdfA1A ToPdfA2A ToPdfA3A ToPdfA3B ToPdfX1A2001
converter.ToPdfA2B(outputFile)
