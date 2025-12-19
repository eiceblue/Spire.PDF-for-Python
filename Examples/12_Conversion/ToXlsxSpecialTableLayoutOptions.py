from spire.pdf import *

inputFile = "./Demos/Data/ToXlsxOptions.pdf"
outputFile = "out.xlsx"


# Create a new PdfDocument object to represent the PDF file
pdf = PdfDocument()

# Load the PDF document from the specified input file path
pdf.LoadFromFile(inputFile)

# Set the XlsxSpecialTableLayoutOptions as the conversion options for PDF to XLSX conversion
options = XlsxSpecialTableLayoutOptions(False, False, False)

# Save the PDF document as an Excel file using the specified format and options
pdf.SaveToFile(outputFile, FileFormat.XLSX)

# Release all resources associated with the PdfDocument object
pdf.Dispose()