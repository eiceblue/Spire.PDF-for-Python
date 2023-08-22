from spire.pdf.common import *
from spire.pdf import *

inputFile  =  "./Demos/Data/CustomDocumentProperties.pdf"
outputFile = "CustomDocumentProperties.pdf"

doc = PdfDocument()
#Load a pdf file from disk
doc.LoadFromFile(inputFile)
#Custom document properties
doc.DocumentInformation.SetCustomProperty("Company", "E-iceblue")
doc.DocumentInformation.SetCustomProperty("Component", "Spire.PDF for .NET")
doc.DocumentInformation.SetCustomProperty("Name", "Daisy")
doc.DocumentInformation.SetCustomProperty("Team", "SalesTeam")
#Save to file
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()