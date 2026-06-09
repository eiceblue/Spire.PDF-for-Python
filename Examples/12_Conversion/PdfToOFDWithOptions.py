from spire.pdf.common import *
from spire.pdf import *

inputFile = "data/Sample.pdf"
outputFile = "PDFToOFDWithOptions.ofd"

# Initialize a new instance of the PdfDocument class to handle PDF operations.
pdf = PdfDocument()

# Load the PDF document from the specified input file path.
pdf.LoadFromFile(inputFile)

# Create an instance of OfdOptions to configure settings for converting PDF to OFD format.
ofdOptions = OfdOptions()

# Enable the use of temporary file storage during the conversion process to handle large files or complex layouts.
ofdOptions.UseTempFileStorage = True

# Apply the configured OFD conversion options to the PDF document's conversion settings.
pdf.ConvertOptions.SetPdfToOfdOptions(ofdOptions)

# Save the loaded PDF document as an OFD file to the specified output path.
pdf.SaveToFile(outputFile, FileFormat.OFD)

# Close the PDF document and release all associated resources.
pdf.Close()