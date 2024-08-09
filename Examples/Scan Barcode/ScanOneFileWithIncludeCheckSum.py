from spire.barcode import *

def WriteAllText(fpath:str,content:str):
    with open(fpath,'w',encoding="utf-8") as fp:
        fp.write(content)

strCode = BarcodeScanner.ScanOneFileWithIncludeCheckSum("QRCode.png",True)
WriteAllText("ScanOneFileWithIncludeCheckSum.txt",strCode)