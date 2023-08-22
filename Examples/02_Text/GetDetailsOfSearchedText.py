from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/SearchReplaceTemplate.pdf"
outputFile = "GetDetailsOfSearchedText_out.txt"

doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page of pdf file
page = doc.Pages[0]
# Create PdfTextFindCollection object to find all the matched phrases
collection = page.FindText("Spire.PDF for Python", TextFindParameter.IgnoreCase)
# Create a StringBuilder object to put the details of the text searched
builder = []
for find in collection.Finds:
    builder.append("=================================================================================="+"\n")
    builder.append("Match Text: " + find.MatchText+"\n")
    builder.append("Text: " + find.SearchText+"\n")
    builder.append("Size: " + find.Size.ToString()+"\n")
    builder.append("Position: " + find.Position.ToString()+"\n")
    builder.append("The index of page which is including the searched text : " + str(find.SearchPageIndex)+"\n")
    builder.append("The line that contains the searched text : " + find.LineText+"\n")
    builder.append("Match Text: " + find.MatchText+"\n")
WriteAllText(outputFile, builder)
doc.Close()
