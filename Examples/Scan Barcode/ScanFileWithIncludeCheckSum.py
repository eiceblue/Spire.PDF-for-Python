from spire.barcode import *


def AppendAllText(fname:str,text:List[str]):
    fp = open(fname,"w")
    for s in text:
        fp.write(s )
    fp.close()

strCode = BarcodeScanner.ScanFileWithIncludeCheckSum("QRCode.png",True)
AppendAllText("ScanFileWithIncludeCheckSum.txt",strCode)