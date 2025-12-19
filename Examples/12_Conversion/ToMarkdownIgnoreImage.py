from spire.pdf import *

inputFile = "./Demos/Data/DeleteImage.pdf"
outputFile = "out2.md"


# Create an instance of PdfToMarkdownConverter with the input PDF file
converter = PdfToMarkdownConverter(inputFile)

# Configure the converter to skip processing images in the PDF
converter.MarkdownOptions.IgnoreImage = True

# Convert the PDF content to Markdown format and save to the output file
converter.ConvertToMarkdown(outputFile)