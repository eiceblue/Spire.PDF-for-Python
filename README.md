# Independent Python API for PDF Creating, Editing, and Converting

[![Foo](https://i.imgur.com/dLzlPI2.png)](https://www.e-iceblue.com/Introduce/pdf-for-python.html)

[Product Page](https://www.e-iceblue.com/Introduce/pdf-for-python.html) | Documentation | Examples | [Forum](https://www.e-iceblue.com/forum/spire-pdf-f7.html) | [Temporary License](https://www.e-iceblue.com/TemLicense.html) | [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)

[Spire.PDF for Python](https://www.e-iceblue.com/Introduce/pdf-for-python.html) is an independent Python API that enables developers to create, read, edit, save, and convert PDF files in Python programs. It provides developers with various functions to process PDF documents without any other dependencies.

[Spire.PDF for Python](https://www.e-iceblue.com/Introduce/pdf-for-python.html) supports various PDF features including security settings, extracting text/image from PDF, merging/splitting PDF, drawing text/image/shape/barcode to PDF, creating and filling in form fields, adding tables to PDF, compressing PDF documents, etc. 

With this professional Python API, developers can also easily convert PDF to XPS, XPS to PDF, PDF to SVG, SVG to PDF, PDF to Excel, PDF to Word, PDF to HTML, HTML to PDF and PDF to PDF/A in high quality.

### Support for Various PDF Versions
- PDF 1.2 to PDF 1.7
- PDF/A - 1b
- PDF/x1a
- PDF/A1
- PDF/A2
- PDF/A3
- PDF/UA

### High-Fidelity PDF File Conversion
- Convert HTML to PDF
- Convert HTML to PDF
- Convert Image to PDF
- Convert Text to PDF
- Convert PDF to HTML
- Convert XPS to PDF
- Convert PDF to SVG
- Convert PDF to XPS
- Convert PDF to Image
- Convert PDF to Word
- Convert PDF to Excel

### Security Features
Spire.PDF for Python can protect PDF documents by setting passwords and adding digital signatures. User password and owner password can determine the encrypted PDF documents readability, modifiability, printability and other selective restrictions. And digital signatures can ensure the authenticity and integrity of PDF documents, and confirm the identity in document exchange.

## Examples

### Create a PDF document in Python
```Python
﻿from spire.pdf.common import *
from spire.pdf import *

outputFile = "HelloWorld.pdf"

#Create a pdf document
doc= PdfDocument()
#Create one page
page = doc.Pages.Add()
s = "Hello, World"
x = 10.0
y = 10.0
font = PdfFont(PdfFontFamily.Helvetica ,30.0)
color = PdfRGBColor(Color.get_Black())
textBrush = PdfSolidBrush(color)
#Draw the text
page.Canvas.DrawString(s, font, textBrush, x, y)
#Save the document
doc.SaveToFile(outputFile)
doc.Close()
```

### Convert PDF to Word
```Python
from spire.pdf.common import *
from spire.pdf import *

outputFile = "ToDocx.docx"
inputFile = "./Demos/Data/ToDocx.pdf"

# Load a pdf document
inputfile = inputFile
doc = PdfDocument()
doc.LoadFromFile(inputfile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.DOCX)
doc.Close()
```

### Add a watermark to PDF
```Python
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/ImageWaterMark.pdf"
outputFile = "TextWaterMark.pdf"

#Create a pdf document and load file from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first page
page = doc.Pages[0]
#Draw text watermark
brush = PdfTilingBrush(SizeF(page.Canvas.ClientSize.Width / float(2), page.Canvas.ClientSize.Height / float(3)))
brush.Graphics.SetTransparency(0.3)
brush.Graphics.Save()
brush.Graphics.TranslateTransform(brush.Size.Width / float(2), brush.Size.Height / float(2))
brush.Graphics.RotateTransform(-45.0)
brush.Graphics.DrawString("Spire.Pdf Demo", PdfFont(PdfFontFamily.Helvetica, 24.0), PdfBrushes.get_Violet(), 0.0, 0.0, PdfStringFormat(PdfTextAlignment.Center))
brush.Graphics.Restore()
brush.Graphics.SetTransparency(1.0)
page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize))
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()
```

### Add a stamp to PDF
```Python
from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/AddTextStamp.pdf"
outputFile = "AddTextStamp_out.pdf"

#Open a pdf document
document = PdfDocument()
document.LoadFromFile(inputFile)
#Get the first page
page = document.Pages[0]
#Create a pdf template
template = PdfTemplate(125.0, 55.0)
font1 = PdfTrueTypeFont("Elephant", 10.0, PdfFontStyle.Italic, True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkRed()))
pen = PdfPen(brush)
rectangle = RectangleF(PointF(5.0, 5.0), template.Size)
CornerRadius = 20.0
path = PdfPath()
path.AddArc(template.GetBounds().X, template.GetBounds().Y, CornerRadius, CornerRadius, 180.0, 90.0)
path.AddArc(template.GetBounds().X + template.Width - CornerRadius, template.GetBounds().Y, CornerRadius, CornerRadius, 270.0, 90.0)
path.AddArc(template.GetBounds().X + template.Width - CornerRadius, template.GetBounds().Y + template.Height - CornerRadius, CornerRadius, CornerRadius, 0.0, 90.0)
path.AddArc(template.GetBounds().X, template.GetBounds().Y + template.Height - CornerRadius, CornerRadius, CornerRadius, 90.0, 90.0)
path.AddLine(template.GetBounds().X, template.GetBounds().Y + template.Height - CornerRadius, template.GetBounds().X, template.GetBounds().Y + CornerRadius / float(2))
template.Graphics.DrawPath(pen, path)
#Draw stamp text
s1 = "REVISED\n"
s2 = "by E-iceblue at " + DateTime.get_Now().ToString("MM dd, yyyy")
template.Graphics.DrawString(s1, font1, brush, PointF(5.0, 10.0))
font2 = PdfTrueTypeFont("Lucida Sans Unicode", 9.0, PdfFontStyle.Bold, True)
template.Graphics.DrawString(s2, font2, brush, PointF(2.0, 30.0))
#Create a rubber stamp
stamp = PdfRubberStampAnnotation(rectangle)
apprearance = PdfAppearance(stamp)
apprearance.Normal = template
stamp.Appearance = apprearance
#Draw stamp into page
page.AnnotationsWidget.Add(stamp)
#Save pdf document
document.SaveToFile(outputFile)
document.Close()
```

[Product Page](https://www.e-iceblue.com/Introduce/pdf-for-python.html) | Documentation | Examples | [Forum](https://www.e-iceblue.com/forum/spire-pdf-f7.html) | [Temporary License](https://www.e-iceblue.com/TemLicense.html) | [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)
