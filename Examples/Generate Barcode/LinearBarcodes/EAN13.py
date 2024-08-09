from spire.barcode import *

def WriteAllBytes(fname:str,data):
    fp = open(fname,"wb")
    fp.write(data)
    fp.close()

barcodeSettings= BarcodeSettings()
barcodeSettings.Type = BarCodeType.EAN13
barcodeSettings.Data = "12345"
barCodeGenerator = BarCodeGenerator(barcodeSettings)
barcodeimage = barCodeGenerator.GenerateImage()
WriteAllBytes("EAN13.png",barcodeimage)
