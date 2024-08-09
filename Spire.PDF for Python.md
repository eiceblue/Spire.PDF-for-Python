# Comprehensive PDF Manipulation Class Library for Python

[![Foo](https://i.imgur.com/dLzlPI2.png)](https://www.e-iceblue.com/Introduce/pdf-for-python.html)

[Product Page](https://www.e-iceblue.com/Introduce/pdf-for-python.html) | [Documentation](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Spire.PDF-for-Python-Program-Guide-Content.html) | [Examples](https://github.com/eiceblue/Spire.PDF-for-Python) | [Forum](https://www.e-iceblue.com/forum/spire-pdf-f7.html) | [Temporary License](https://www.e-iceblue.com/TemLicense.html) | [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)

[Spire.PDF for Python](https://www.e-iceblue.com/Introduce/pdf-for-python.html) is a robust and versatile PDF manipulation library designed to simplify PDF reading, creation, editing, conversion, and management tasks within Python applications. Developed by E-iceblue, this reliable package offers a complete suite of tools enabling developers to effortlessly build solutions for working with PDF documents in Python programs.

This Python library empowers users to streamline document workflows by providing a rich set of APIs that facilitate seamless integration with enterprise-level PDF processing needs. It supports a wide array of advanced features without the need for any external dependencies, ensuring compatibility and performance consistency.

## Core Features & Functionality
###Installation

pip install Spire.Pdf

### Extensive PDF Version Support
- PDF 1.2 to PDF 1.7
- PDF/A - 1b
- PDF/x1a
- PDF/A1
- PDF/A2
- PDF/A3
- PDF/UA

### Flexible PDF Document Conversions
- [Convert PDF to images](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Images-JPG-PNG-BMP.html) (PNG, JPG, BMP, etc.) for wide distribution
- [Convert PDF to Word documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Word-DOC-or-DOCX.html) for easy content editing
- [Convert PDF to Excel workbooks](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Excel.html) for convenient data processing
- [Convert PDF to SVG](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-SVG.html) and many other formats effortlessly

### Main Tutorials

- [How to Extract Image From a PDF in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Extract/Read/Python-Extract-Text-and-Images-from-PDF-Documents.html)
- [How to Extract Text From a PDF in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Extract/Read/Python-Extract-Text-from-a-PDF-Document.html)
- [How to Rotate PDF Pages in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Split-a-PDF-File-into-Multiple-PDFs.html)
- [How to Merge PDFs in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Merge-PDF-Documents.html)
- [How to Split PDFs in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Split-a-PDF-File-into-Multiple-PDFs.html)
- [How to Add Text Watermarks in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Watermark/Python-Add-Text-Watermarks-to-PDF-Documents.html)
- [How to Add Image Watermarks in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Watermark/Python-Add-Image-Watermarks-to-PDF-Documents.html）
- [How to Encrypt a PDF in Python](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Security/Python-Protect-or-Unprotect-PDF-Documents.html)


### Solid PDF Security Measures
- [Protect PDF documents with passwords](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Security/Python-Protect-or-Unprotect-PDF-Documents.html) for secure sharing
- Set PDF security permissions to control access and usage
- Sign PDF documents with digital signature for certified trust

### Efficient PDF Construction & Manipulation
- Create new PDF documents with customizable attributes and layouts
- [Merge multiple PDFs into one PDF](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Merge-PDF-Documents.html) or [split a PDF into separate PDFs](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Document-Operation/Python-Split-a-PDF-File-into-Multiple-PDFs.html)

### Effortless PDF Content Extraction
- [Extract text from PDFs](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Extract/Read/Python-Extract-Text-from-a-PDF-Document.html) with simple Python code
- [Extract images from PDFs](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Extract/Read/Python-Extract-Text-and-Images-from-PDF-Documents.html) for further editing and utilization

## Code Examples

### Create PDF Documents
```python
from spire.pdf.common import *
from spire.pdf import *

outputFile = "HelloWorld.pdf"

# Create a pdf document
doc= PdfDocument()
# Create one page
page = doc.Pages.Add()
s = "Hello, World"
x = 10.0
y = 10.0
font = PdfFont(PdfFontFamily.Helvetica ,30.0)
color = PdfRGBColor(Color.get_Black())
textBrush = PdfSolidBrush(color)
# Draw the text
page.Canvas.DrawString(s, font, textBrush, x, y)
# Save the document
doc.SaveToFile(outputFile)
doc.Close()
```

### [Convert PDFs to Word Documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-Word-DOC-or-DOCX.html)
```python
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

### [Encrypt PDF Documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Security/Python-Protect-or-Unprotect-PDF-Documents.html)
```python
from spire.pdf.common import *
from spire.pdf import *

# Create a PdfDocument object
doc = PdfDocument()

# Load a sample PDF file
doc.LoadFromFile("input.pdf")

# Encrypt the PDF file with an open password and a permission password
doc.Security.Encrypt("openPsd", "permissionPsd", PdfPermissionsFlags.FillFields, PdfEncryptionKeySize.Key128Bit)

# Save the result file
doc.SaveToFile("output/Encrypted.pdf", FileFormat.PDF)
```

### [Extract Text from PDF Documents](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Extract/Read/Python-Extract-Text-from-a-PDF-Document.html)
```python
from spire.pdf.common import *
from spire.pdf import *

def WriteAllText(fname:str,text:List[str]):
        fp = open(fname,"w")
        for s in text:
            fp.write(s)
        fp.close()

inputFile = "./Demos/Data/PDFTemplate-Az.pdf"
outputFile = "ExtractTextFromParticularPage_out.txt"


doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)
# Get the first page
page = doc.Pages[0]
# Extract text from page keeping white space
text = page.ExtractText(True)
# Write a line of text to the file
WriteAllText(outputFile, text)
doc.Close()
```

[Product Page](https://www.e-iceblue.com/Introduce/pdf-for-python.html) | [Documentation](https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Spire.PDF-for-Python-Program-Guide-Content.html) | [Examples](https://github.com/eiceblue/Spire.PDF-for-Python) | [Forum](https://www.e-iceblue.com/forum/spire-pdf-f7.html) | [Temporary License](https://www.e-iceblue.com/TemLicense.html) | [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)