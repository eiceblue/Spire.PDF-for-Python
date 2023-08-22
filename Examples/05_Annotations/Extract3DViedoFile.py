from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/3D.pdf"

#Load old PDF from disk.
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
#Get the first page.
firstPage = pdf.Pages[0]
#Get the annotation collection of the first page
annot = firstPage.AnnotationsWidget
#Define an int variable
count = 0
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, Pdf3DAnnotation):
            annot3D = annot[i] if isinstance(annot[i], Pdf3DAnnotation) else None
            #Get the 3D video data
            strData = annot3D._3DData
            if strData is not None:
                #Write the data into .u3d format file
                strData.Save("""3d-{0:d}.u3d""".format(count))
                count += 1
pdf.Close()
