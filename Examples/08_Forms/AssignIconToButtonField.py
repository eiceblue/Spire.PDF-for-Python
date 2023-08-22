from spire.pdf.common import *
from spire.pdf import *

inputImage1 = "./Demos/Data/E-iceblueLogo.png"
inputImage2 = "./Demos/Data/PdfImage.png"
inputImage3 = "./Demos/Data/PDFJAVA.png"
outputFile = "AssignIconToButtonField-result.pdf"

# Create a PDF document
doc = PdfDocument()
page = doc.Pages.Add()
# Create a Button
btn = PdfButtonField(page, "button1")
btn.Bounds = RectangleF(0.0, 50.0, 120.0, 100.0)
btn.HighlightMode = PdfHighlightMode.Push
btn.LayoutMode = PdfButtonLayoutMode.CaptionOverlayIcon
# Set text and icon for Normal appearance
btn.Text = "Normal Text"
btn.Icon = PdfImage.FromFile(inputImage1)
# Set text and icon for Click appearance (Can only be set when highlight mode is Push)
btn.AlternateText = "Alternate Text"
btn.AlternateIcon = PdfImage.FromFile(inputImage2)
# Set text and icon for Rollover appearance (Can only be set when highlight mode is Push)
btn.RolloverText = "Rollover Text"
btn.RolloverIcon = PdfImage.FromFile(inputImage3)
# Set icon layout
btn.IconLayout.Spaces = [0.5, 0.5]
btn.IconLayout.ScaleMode = PdfButtonIconScaleMode.Proportional
btn.IconLayout.ScaleReason = PdfButtonIconScaleReason.Always
btn.IconLayout.IsFitBounds = False
# Add the button to the document
doc.Form.Fields.Add(btn)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
