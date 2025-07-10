from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/ExtractTextFromSpecificArea.pdf"
outputFile = "ExtractTextFromSpecificArea_out.txt"

# Load the PDF file
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)

# Get the first page
page = pdf.Pages[0]

# Extract text from a specific rectangular area within the page
pdfTextExtractor=PdfTextExtractor(page)
pdfTextExtractOptions=PdfTextExtractOptions()
pdfTextExtractOptions.ExtractArea=RectangleF(80.0, 180.0, 500.0, 200.0)
text=pdfTextExtractor.ExtractText(pdfTextExtractOptions)

# Save the text to a .txt file
sb = []
sb.append(text)
WriteAllText(outputFile, sb)
pdf.Close()

