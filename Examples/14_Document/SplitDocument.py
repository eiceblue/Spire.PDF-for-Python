from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/SplitDocument.pdf"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
pattern = "SplitDocument-{0}.pdf"
#Split document
doc.Split(pattern)
lastPageFileName = ("SplitDocument-{0:d}.pdf").format(doc.Pages.Count - 1)
doc.Close()
