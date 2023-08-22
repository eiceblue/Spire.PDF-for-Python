from spire.pdf.common import *
from spire.pdf import *


inputFile1 = "./Demos/Data/SampleB_1.pdf"
inputFile2 = "./Demos/Data/template.svg"
outputFile = "AddSVGToPDF_out.pdf"

#Create a new PDF document.
existingPDF = PdfDocument()
#Load an existing PDF
existingPDF.LoadFromFile(inputFile1)
#Create a new PDF document.
doc = PdfDocument()
#Load the SVG file
doc.LoadFromSvg(inputFile2)
#Create template
template = doc.Pages[0].CreateTemplate()
#Draw template on existing PDF
existingPDF.Pages[0].Canvas.DrawTemplate(doc.Pages[0].CreateTemplate(), PointF(50.0, 350.0), SizeF(200.0, 200.0))
#Save the document       
existingPDF.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
existingPDF.Close()