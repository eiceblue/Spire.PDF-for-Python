from spire.pdf.common import *
from spire.pdf import *

# Path to the output PDF file
outputFile = "AddListBoxField.pdf"  

# Create a PdfDocument object
doc = PdfDocument()

# Add a page
page = doc.Pages.Add()

# Initialize x and y coordinates
baseX = 100.0
baseY = 30.0

# Create two brush objects
brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))

# Create a font
font = PdfFont(PdfFontFamily.TimesRoman, 12.0, PdfFontStyle.Regular)

# Add label for the listbox
page.Canvas.DrawString("ListBox:", font, brush, PointF(10.0, baseY))  
listboxBound = RectangleF(baseX, baseY, 150.0, 50.0)

# Initialize a PdfListBoxField object
listBoxField = PdfListBoxField(page, "listbox") 

# Add items to the listbox
listBoxField.Items.Add(PdfListFieldItem("Item 1", "item1"))  
listBoxField.Items.Add(PdfListFieldItem("Item 2", "item2"))  
listBoxField.Items.Add(PdfListFieldItem("Item 3", "item3")) 

# Set the bounds of the listbox
listBoxField.Bounds = listboxBound  

# Set the font of the listbox
listBoxField.Font = font  

# Set the selected index of the listbox
listBoxField.SelectedIndex = 0  

# Add the listbox field to the document's form fields
doc.Form.Fields.Add(listBoxField)  


# Save to file
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Dispose()