from spire.pdf.common import *
from spire.pdf import *
import io

inputFile = "./Demos/Data/Sample.pdf"
outputFile = "oHTMLStream.html"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Save to HTML stream
fileStream = Stream(outputFile)
doc.SaveToStream(fileStream, FileFormat.HTML)
fileStream.Close()
