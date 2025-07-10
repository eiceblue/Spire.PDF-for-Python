from spire.pdf.common import *
from spire.pdf import *

inputFile1 = "./Demos/Data/EmbedSoundFile.pdf"
inputFile2 = "./Demos/Data/Music.wav"
outputFile = "EmbedSoundFile_out.pdf"

#Create a new PDF document
doc = PdfDocument()
doc.LoadFromFile(inputFile1)
#Add a page
page = doc.Pages[0]
#Create a sound action
soundAction = PdfSoundAction(inputFile2)
soundAction.Sound.Bits = 15
soundAction.Sound.Channels = PdfSoundChannels.Stereo
soundAction.Sound.Encoding = PdfSoundEncoding.Signed
soundAction.Volume = 0.8
soundAction.Repeat = True
# Set the sound action to be executed when the PDF document is opened
doc.AfterOpenAction = soundAction
#Save the document
doc.SaveToFile(outputFile)
doc.Close()