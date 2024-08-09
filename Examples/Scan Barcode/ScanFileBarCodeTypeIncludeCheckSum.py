from spire.barcode import *

def AppendAllText(fname:str,text:List[str]):
    fp = open(fname,"w")
    for s in text:
        fp.write(s )
    fp.close()

strCode = BarcodeScanner.ScanFileBarCodeTypeIncludeCheckSum("QRCode.png",BarCodeType.QRCode,True)
AppendAllText("ScanFileBarCodeTypeIncludeCheckSum.txt",strCode)