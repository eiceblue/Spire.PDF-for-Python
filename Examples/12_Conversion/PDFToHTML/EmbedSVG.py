from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ToHTMLWithEmbedingSVG_out.html"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Set the convertion option to embed image in html
doc.ConvertOptions.SetPdfToHtmlOptions(True)
#Convert to html file
doc.SaveToFile(outputFile, FileFormat.HTML)
doc.Close()