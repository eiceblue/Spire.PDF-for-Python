from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToPDFA.pdf"
inputFile = "./Demos/Data/ToPDFA.pdf"

# Convert to PDFA file
converter = PdfStandardsConverter(inputFile)
converter.ToPdfA1B(outputFile)
