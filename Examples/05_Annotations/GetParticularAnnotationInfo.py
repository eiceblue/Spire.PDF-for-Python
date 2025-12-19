from spire.pdf.common import *
from spire.pdf import *

inputFile = "Data/Template_Pdf_3.pdf"
outputFile = "GetParticularAnnotationInfo.txt"

#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get the annotation collection from the document.
annotations = pdf.Pages[0].AnnotationsWidget
sb = []
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #Get particular annotation information from the document.
        if isinstance(annotation, PdfTextAnnotationWidget):
            sb.append("Annotation information: ")
            sb.append("Annotation text: " + annotation.Text)
            sb.append("Annotation ModifiedDate: " + annotation.ModifiedDate.strftime("%Y/%m/%d %H:%M:%S"))
            sb.append("Annotation author: " + annotation.Author)
            sb.append("Annotation Name: " + annotation.Name)
#Save to file.
with open(outputFile, "w") as file:
    file.write("\n".join(sb))
pdf.Close()
