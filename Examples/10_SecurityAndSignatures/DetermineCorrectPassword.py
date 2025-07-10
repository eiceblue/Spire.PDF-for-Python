from spire.pdf import *

def WriteAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s)
    fp.close()

inputFile = "./Demos/Data/CheckPasswordProtection.pdf"
outputFile = "DetermineCorrectPassword.txt"

stringBuilder=""

# List of potential passwords to check
passwords = ["password1", "password2", "password3", "test", "sample"]

# Iterate through each password
for value in passwords:
    try:
        # Create a new PDF document
        doc = PdfDocument()
        # Load the PDF from file with the current password
        doc.LoadFromFile(inputFile,value)
        # If no exception is thrown, the password is correct
        stringBuilder+="Password = " + value + "  is correct" + "\n"
    except SpireException as e:
        # If an exception is thrown, the password is incorrect
        stringBuilder+="Password = " + value + "  is not correct"+ "\n"

# Write the result to a text file
WriteAllText(outputFile, stringBuilder)