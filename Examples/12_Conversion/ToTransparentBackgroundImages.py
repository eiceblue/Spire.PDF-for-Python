from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToTransparentBackgroundImages.png"
inputFile = "./Demos/Data/ToTransparentBackgroundImages.pdf"

# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Save to images
doc.ConvertOptions.SetPdfToImageOptions(0)
with doc.SaveAsImage(0, PdfImageType.Bitmap) as imageS:
    imageS.Save(outputFile)
doc.Close()
