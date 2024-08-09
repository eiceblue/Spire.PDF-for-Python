from spire.barcode import *

def WriteAllBytes(fname:str,data):
    fp = open(fname,"wb")
    fp.write(data)
    fp.close()

barcodeSettings= BarcodeSettings()
barcodeSettings.Type = BarCodeType.QRCode
barcodeSettings.BackColor = Color.get_WhiteSmoke()
barcodeSettings.QRCodeDataMode = QRCodeDataMode.Byte
barcodeSettings.QRCodeECL = QRCodeECL.M
barcodeSettings.ShowTextOnBottom = True
barcodeSettings.X = 3
data = "ABC 123456789"
barcodeSettings.Data2D = data
barcodeSettings.Data = data
barcodeSettings.SetQRCodeLogoImage("data/Logo.png")
barCodeGenerator = BarCodeGenerator(barcodeSettings)
barcodeimage = barCodeGenerator.GenerateImage()
WriteAllBytes("AddLogoImageQRCode.png",barcodeimage)

