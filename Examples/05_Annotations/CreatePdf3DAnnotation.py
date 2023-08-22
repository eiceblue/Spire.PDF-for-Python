
from spire.pdf.common import *
from spire.pdf import *

inputfile = "./Demos/Data/CreatePdf3DAnnotation.u3d"
outputFile = "CreatePdf3DAnnotation_out.pdf"

#Create a new Pdf document.
doc = PdfDocument()
#Add a new page to it.
page = doc.Pages.Add()
#Draw a rectangle on the page to define the canvas area for the 3D file.
rt = RectangleF(0.0, 80.0, 200.0, 200.0)
#Initialize a new object of Pdf3DAnnotation, load the .u3d file as 3D annotation.
annotation = Pdf3DAnnotation(rt, inputfile)
annotation.Activation = Pdf3DActivation()
annotation.Activation.ActivationMode = Pdf3DActivationMode.PageOpen
#Define a 3D view mode.
View = Pdf3DView()
View.Background = Pdf3DBackground(PdfRGBColor(Color.get_Purple()))
View.ViewNodeName = "3DAnnotation"
View.RenderMode = Pdf3DRendermode(Pdf3DRenderStyle.Solid)
View.InternalName = "3DAnnotation"
View.LightingScheme = Pdf3DLighting()
View.LightingScheme.Style = Pdf3DLightingStyle.Day
#Set the 3D view mode for the annotation.
annotation.Views.Add(View)
#Add the annotation to Pdf.
page.AnnotationsWidget.Add(annotation)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
