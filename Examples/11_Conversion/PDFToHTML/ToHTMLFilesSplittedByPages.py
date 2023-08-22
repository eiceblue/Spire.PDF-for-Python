from spire.pdf.common import *
from spire.pdf import *
import io

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ToHTMLFilesSplittedByPages.html"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Set the convertion option to embed image in html
doc.ConvertOptions.SetPdfToHtmlOptions(False, True, 1)
#Convert to html file
doc.SaveToFile(outputFile, FileFormat.HTML)
doc.Close()