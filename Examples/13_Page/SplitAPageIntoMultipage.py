from spire.pdf.common import *
from spire.pdf import *

outputFile = "SplitAPageIntoMultipage.pdf"
inputFile = "./Demos/Data/PDFTemplate_N.pdf"

#Load Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Create a new Pdf
newPdf = PdfDocument()
#Remove all the margins
newPdf.PageSettings.Margins.All = 0.0
#Set the page size of new Pdf
newPdf.PageSettings.Width = page.Size.Width
newPdf.PageSettings.Height = page.Size.Height / float(2)
#Add a new page
newPage = newPdf.Pages.Add()
format = PdfTextLayout()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
#Draw the page in the new page
page.CreateTemplate().Draw(newPage, PointF(0.0, 0.0), format)
#Save the Pdf document
newPdf.SaveToFile(outputFile)
newPdf.Close()



