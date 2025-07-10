from spire.pdf.common import *
from spire.pdf import *
import glob


inputFile = "./Demos/Data/Sample.pdf"
inputFolder="./Demos/Data/CreatePDFPortfolio/*"
outputFile = "CreatePDFPortfolio.pdf"

#Create folder and sub folder to add file into it
files = glob.glob(inputFolder)
doc = PdfDocument(inputFile)
i = 0
while i < len(files):
    doc.Collection.Folders.AddFile(files[i])
    folder = doc.Collection.Folders.CreateSubfolder("SubFolder" + str(i + 1))
    folder.AddFile(files[i])
    i += 1
#Save the document
doc.SaveToFile(outputFile)
doc.Close()  
