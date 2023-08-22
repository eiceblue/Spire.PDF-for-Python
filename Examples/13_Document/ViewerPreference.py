from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ViewerPreference.pdf"
outputFile = "ViewerPreference.pdf"

#Load pdf document
doc = PdfDocument(inputFile)
#Set view reference
doc.ViewerPreferences.CenterWindow = True
doc.ViewerPreferences.DisplayTitle = False
doc.ViewerPreferences.FitWindow = False
doc.ViewerPreferences.HideMenubar = True
doc.ViewerPreferences.HideToolbar = True
doc.ViewerPreferences.PageLayout = PdfPageLayout.SinglePage
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()