from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/ExtractHighlightedText.pdf"
outputFile = "ExtractHighlightedText.txt"

#Create a pdf document
doc = PdfDocument()
#Load a pdf file
doc.LoadFromFile(inputFile)
page = doc.Pages[0]
textMarkupAnnotation = None
stringBuilder="Extracted hightlighted text:" + '\n'
#Get PdfTextMarkupAnnotationWidget objects
annotations = page.AnnotationsWidget
#Update free text annotation.
if annotations.Count > 0:
    for i in range(annotations.Count):
        textMarkupAnnotation = annotations.get_Item(i)
        if isinstance(textMarkupAnnotation, PdfTextMarkupAnnotationWidget):
            #Get the highlighted text
            stringBuilder+= page.ExtractText(textMarkupAnnotation.Bounds)+ '\n'
            #Get the highlighted color
            color = textMarkupAnnotation.TextMarkupColor
WriteAllText(outputFile,stringBuilder)
doc.Close()
