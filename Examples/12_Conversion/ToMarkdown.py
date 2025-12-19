from spire.pdf import *

inputFile = "./Demos/Data/PDFToMarkDown.pdf"
outputFile = "ToMd.md"

# Load a pdf document

doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to .md file
doc.SaveToFile(outputFile, FileFormat.Markdown)
doc.Close()

