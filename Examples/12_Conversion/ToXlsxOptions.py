from spire.pdf import *

inputFile = "./Demos/Data/ToXlsxOptions.pdf"
outputFile = "out.xlsx"


# Create a new PdfDocument object to represent the PDF file
pdf = PdfDocument()

# Load the PDF document from the specified input file path
pdf.LoadFromFile(inputFile)

# Configure Excel export options:
options = XlsxLineLayoutOptions(False, True, True)

# Save the PDF document as an Excel file using the specified format and options
pdf.SaveToFile(outputFile, FileFormat.XLSX)

# Release all resources associated with the PdfDocument object
pdf.Dispose()

