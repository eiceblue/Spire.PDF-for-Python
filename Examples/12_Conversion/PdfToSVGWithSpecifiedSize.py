from spire.pdf.common import *
from spire.pdf import *

inputFile = "data/Sample.pdf"
outputFile = "toSvg.svg"

# Initialize the converter with the input PDF file path
converter = PdfToSvgConverter(inputFile)

# Set the horizontal scaling factor for the output SVG to 1.0 (no scaling)
converter.SvgOptions.ScaleX = 1.0

# Set the vertical scaling factor for the output SVG to 1.0 (no scaling)
converter.SvgOptions.ScaleY = 1.0

# Perform the conversion from PDF to SVG and save the result to the output file
converter.Convert(outputFile)
