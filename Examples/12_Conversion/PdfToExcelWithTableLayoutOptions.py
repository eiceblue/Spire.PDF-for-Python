from spire.pdf.common import *
from spire.pdf import *

inputFile = "data/ToXlsxOptions.pdf"
outputFile = "XlsxSpecialTableLayoutOptions.xlsx"

# Create a new instance of the PdfDocument class to handle PDF operations
pdf = PdfDocument()

# Load the PDF file from the specified input file path
pdf.LoadFromFile(inputFile)

# Initialize table layout options for the conversion:
# False (Enable convertToMultipleSheet), False (Disable rotatedText), False (Disable overlapText)
options = XlsxSpecialTableLayoutOptions(False, False, False)

# Configure the conversion settings by applying the defined table layout options for PDF to XLSX conversion
pdf.ConvertOptions.SetPdfToXlsxOptions(options)

# Save the converted document to the specified output file in XLSX (Excel) format
pdf.SaveToFile(outputFile, FileFormat.XLSX)

# Close the document and release any associated resources
pdf.Close()