from spire.pdf.common import *
from spire.pdf import *

inputFile = "data/ToXlsxOptions.pdf"
outputFile = "PdfToExcelWithLineLayoutOptions.xlsx"

# Create a new instance of the PdfDocument class to handle PDF operations
pdf = PdfDocument()

# Load the PDF file from the specified input file path
pdf.LoadFromFile(inputFile)

# Initialize line layout options for the conversion:
# True (Enable convertToMultipleSheet), False (Disable rotatedText), False (Disable splitCell), False (Disable wrapText), False (Disable overlapText) 
lineOption = XlsxLineLayoutOptions(True, False, True, True, True)

# Configure the conversion settings by applying the defined line layout options for PDF to XLSX conversion
pdf.ConvertOptions.SetPdfToXlsxOptions(lineOption)

# Save the converted document to the specified output file in XLSX (Excel) format
pdf.SaveToFile(outputFile, FileFormat.XLSX)

# Close the document and release any associated resources
pdf.Close()