from spire.pdf import *

def WriteAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s)
    fp.close()

inputFile = "./Demos/Data/CheckPasswordProtection.pdf"
outputFile = "CheckPasswordProtection.txt"

# Check if the document is password protected
isProtected = PdfDocument.IsPasswordProtected(inputFile)

# Determine the message based on whether the document is protected
word = "password " if isProtected else "not password "
stringBuilder = "The pdf is " + word + "protected!"

# Write the result to a text file
WriteAllText(outputFile, stringBuilder)