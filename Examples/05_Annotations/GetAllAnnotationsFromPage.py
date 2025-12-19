from spire.pdf.common import *
from spire.pdf import *

inputFile = "Data/Template_Pdf_3.pdf"
outputFile = "GetAllAnnotationsFromPage.txt"

#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get all annotations from the first page.
annotations = pdf.Pages[0].AnnotationsWidget
sb = []
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, PdfPopupAnnotationWidget):
            continue
        sb.append("Annotation information: ")
        sb.append("Text: " + annotation.Text)
        modifiedDate = annotation.ModifiedDate.strftime("%Y/%m/%d %H:%M:%S")
        sb.append("ModifiedDate: " + modifiedDate)
#Save to file.
with open(outputFile, "w") as file:
    file.write("\n".join(sb))
pdf.Close()
