from spire.barcode import *

def WriteAllBytes(fname:str,data):
    fp = open(fname,"wb")
    fp.write(data)
    fp.close()

barcodeSettings= BarcodeSettings()
barcodeSettings.Type = BarCodeType.RoyalMail4State
barcodeSettings.Data = "12345"
barCodeGenerator = BarCodeGenerator(barcodeSettings)
barcodeimage = barCodeGenerator.GenerateImage()
WriteAllBytes("RoyalMail4State.png",barcodeimage)
