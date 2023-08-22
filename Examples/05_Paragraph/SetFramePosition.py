﻿from spire.doc import *
from spire.doc.common import *


inputFile = "./Data/TextInFrame.docx"
outputFile = "SetFramePosition.docx"


#Create a document
document = Document()

#Load the document from disk
document.LoadFromFile(inputFile)

#Get a paragraph
paragraph = document.Sections[0].Paragraphs[0]

#Set the Frame's position
if paragraph.Format.IsFrame:
    paragraph.Format.Frame.SetHorizontalPosition(150)
    paragraph.Format.Frame.SetVerticalPosition(150)

#Save to file.
document.SaveToFile(outputFile, FileFormat.Docx2013)
document.Close()