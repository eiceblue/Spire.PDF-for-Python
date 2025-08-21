# Python代码核心功能提取

# spire.pdf python hello world
## create a simple pdf document with hello world text
```python
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
```

---

# Spire.PDF Python Add Border to Text
## Add border around text in PDF document
```python
#Get the first page
page = doc.Pages[0]
text = "Hello, World2!"
font = PdfTrueTypeFont("Times New Roman", 11.0, PdfFontStyle.Regular,True)
size = font.MeasureString(text)
color = PdfRGBColor(Color.get_Black())
brush = PdfSolidBrush(color)
x = 60.0
y = 600.0
#Draw the text on page
page.Canvas.DrawString(text, font, brush, x, y)
#Draw border for text  
page.Canvas.DrawRectangle(PdfPen(brush, 0.5),RectangleF(x, y, size.Width, size.Height))
```

---

# Spire.PDF Tooltip for Text
## Add tooltip to text in PDF document
```python
#Create a pdf document
doc = PdfDocument()
#Create one page
page = doc.Pages.Add()

#Define the text and its style
text1 = "Your Office Development Master"
font1 = PdfTrueTypeFont("Arial",18.0,PdfFontStyle.Regular,True)
sizeF1 = font1.MeasureString(text1)
rec1 = RectangleF(PointF(100.0,100.0), sizeF1)
#Draw text 
page.Canvas.DrawString(text1, font1, PdfSolidBrush(PdfRGBColor(Color.get_Blue())), rec1)
#Create invisible button on text position
field1 = PdfButtonField(page, "field1")
#Set the bounds and size of field
field1.Bounds = rec1
#Set tooltip content
field1.ToolTip = "E-iceblue Co. Ltd., a vendor of .NET, Java, C++ and Python development components"
#Set no border for field
field1.BorderWidth = 0.0
#Set backcolor and forcolor for field
field1.BackColor = PdfRGBColor(Color.get_Transparent())
field1.ForeColor = PdfRGBColor(Color.get_Transparent())
field1.LayoutMode = PdfButtonLayoutMode.IconOnly
field1.IconLayout.IsFitBounds = True

#Define the text and its style 
text2 = "Spire.PDF"
font2 = PdfFont(PdfFontFamily.TimesRoman, 20.0)
sizeF2 = font2.MeasureString(text2)
rec2 = RectangleF(PointF(100.0, 160.0), sizeF2)
#Draw text 
page.Canvas.DrawString(text2, font2, PdfBrushes.get_DarkOrange(), rec2)
#Create invisible button on text position
field2 = PdfButtonField(page, "field2")
field2.Bounds = rec2
field2.ToolTip = "A professional PDF library applied to creating," + "writing, editing, handling and reading PDF files" + "without any external dependencies within python application."
field2.BorderWidth = 0.0
field2.BackColor = PdfRGBColor(Color.get_Transparent())
field2.ForeColor = PdfRGBColor(Color.get_Transparent())
field2.LayoutMode = PdfButtonLayoutMode.IconOnly
field2.IconLayout.IsFitBounds = True

#Add the buttons to pdf form
doc.AllowCreateForm = True
doc.Form.Fields.Add(field1)
doc.Form.Fields.Add(field2)
```

---

# PDF Transparent Text Addition
## Add transparent text to a PDF document using Spire.PDF for Python
```python
# Create a PDF document
doc = PdfDocument()
# Create one A4 page
page = doc.Pages.Add(PdfPageSize.A4(), PdfMargins(0.0))
page.Canvas.Save()
# Set alpha value
alpha = 0.25
page.Canvas.SetTransparency(alpha, alpha, PdfBlendMode.Normal)
# Create rectangle with specified dimensions      
rect = RectangleF(50.0, 50.0, 450.0, page.Size.Height)
# Create transparent text
text = "Spire.PDF for Python is a professional PDF development component that enables developers to"+ " create, read, edit, convert, and save PDF files in Python programs"+ " without depending on any external applications or libraries."
text += "\n\n\n\n\n"
text += "Spire.PDF for Python supports various PDF processing features including"+ "security settings, extracting text/image from PDF, merging/splitting PDF, drawing text/image/shape/barcode to PDF, etc."+ "in python applications without using Adobe Acrobat."
# Create brush from color channel
brush = PdfSolidBrush(PdfRGBColor(Color.FromArgb(30, 0, 255, 0)))
# Draw the text
page.Canvas.DrawString(text, PdfFont(PdfFontFamily.Helvetica, 14.0), brush, rect)
page.Canvas.Restore()
```

---

# Spire.PDF Python Text Rotation
## Draw rotated text on PDF canvas
```python
# Create PDF document and page
doc = PdfDocument()
page = doc.Pages.Add()

# Set up font and color
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
color = PdfRGBColor(Color.get_Blue())
brush = PdfSolidBrush(color)
text = "This is a text"

# Draw normal text
page.Canvas.DrawString(text, font, brush, 20.0, 30.0)

# Rotate 90 degrees clockwise
state = page.Canvas.Save()
point1 = PointF(20.0, 30.0)
page.Canvas.RotateTransform(90.0, point1)
page.Canvas.DrawString(text, font, brush, 20.0, 30.0)
page.Canvas.Restore(state)

# Rotate 90 degrees counterclockwise
state2 = page.Canvas.Save()
point2 = PointF(20.0, 150.0)
page.Canvas.RotateTransform(-90.0, point2)
page.Canvas.DrawString(text, font, brush, 20.0, 150.0)
page.Canvas.Restore(state2)
```

---

# Spire.PDF Text Drawing
## Demonstrate various text drawing and manipulation techniques in PDF documents
```python
def DrawText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw text - brush
    text = "Go! Turn Around! Go! Go! Go!"
    pen = PdfPens.get_DeepSkyBlue()
    brush = PdfSolidBrush(PdfRGBColor(Color.get_White()))
    format = PdfStringFormat()
    font = PdfFont(PdfFontFamily.Helvetica, 18.0, PdfFontStyle.Italic)
    size = font.MeasureString(text, format)
    rctg = RectangleF(page.Canvas.ClientSize.Width / float(2) + 10, 180.0, size.Width / 3 * 2, size.Height * 2)
    page.Canvas.DrawString(text, font, pen, brush, rctg, format)
    #Restore graphics
    page.Canvas.Restore(state)

def TransformText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw the text - transform    
    font = PdfFont(PdfFontFamily.Helvetica, 18.0)
    brush1 = PdfSolidBrush(PdfRGBColor(Color.get_DeepSkyBlue()))
    brush2 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
    page.Canvas.TranslateTransform(20.0, 200.0)
    page.Canvas.ScaleTransform(1.0, 0.6)
    page.Canvas.SkewTransform(-10, 0.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush1, 0.0, 0.0)
    page.Canvas.SkewTransform(10.0, 0.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush2, 0.0, 0.0)
    page.Canvas.ScaleTransform(1.0, -1.0)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush2, 0.0, -2 * 18.0)
    #Restore graphics
    page.Canvas.Restore(state)

def AlignText(page):
    #Draw the text - alignment
    font = PdfFont(PdfFontFamily.Helvetica, 20.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    leftAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Left!", font, brush, 0.0, 20.0, leftAlignment)
    page.Canvas.DrawString("Left!", font, brush, 0.0, 50.0, leftAlignment)
    rightAlignment = PdfStringFormat(PdfTextAlignment.Right, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Right!", font, brush, page.Canvas.ClientSize.Width, 20.0, rightAlignment)
    page.Canvas.DrawString("Right!", font, brush, page.Canvas.ClientSize.Width, 50.0, rightAlignment)
    centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, page.Canvas.ClientSize.Width / float(2), 40.0, centerAlignment)

def AlignTextInRectangle(page):
    #Draw the text - align in rectangle
    font = PdfFont(PdfFontFamily.Helvetica, 10.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    rctg1 = RectangleF(0.0, 70.0, page.Canvas.ClientSize.Width / float(2), 100.0)
    rctg2 = RectangleF(page.Canvas.ClientSize.Width / float(2), 70.0, page.Canvas.ClientSize.Width / float(2), 100.0)
    page.Canvas.DrawRectangle(PdfSolidBrush(PdfRGBColor(Color.get_LightBlue())), rctg1)
    page.Canvas.DrawRectangle(PdfSolidBrush(PdfRGBColor(Color.get_LightSkyBlue())), rctg2)
    leftAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Top)
    page.Canvas.DrawString("Left! Left!", font, brush, rctg1, leftAlignment)
    page.Canvas.DrawString("Left! Left!", font, brush, rctg2, leftAlignment)
    rightAlignment = PdfStringFormat(PdfTextAlignment.Right, PdfVerticalAlignment.Middle)
    page.Canvas.DrawString("Right! Right!", font, brush, rctg1, rightAlignment)
    page.Canvas.DrawString("Right! Right!", font, brush, rctg2, rightAlignment)
    centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Bottom)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, rctg1, centerAlignment)
    page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, rctg2, centerAlignment)

def RotateText(page):
    #Save graphics state
    state = page.Canvas.Save()
    #Draw the text - transform    
    font = PdfFont(PdfFontFamily.Helvetica, 10.0)
    brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
    centerAlignment = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    x = page.Canvas.ClientSize.Width / float(2)
    y = 380.0
    page.Canvas.TranslateTransform(x, y)
    for i in range(0, 12):
        page.Canvas.RotateTransform(30.0)
        page.Canvas.DrawString("Go! Turn Around! Go! Go! Go!", font, brush, 20.0, 0.0, centerAlignment)
    #Restore graphics
    page.Canvas.Restore(state)
```

---

# Spire.PDF Drawing Text with Gradient
## Draw text with gradient effect in PDF document
```python
#Create a pdf document
doc = PdfDocument()
#Add a new page
page = doc.Pages.Add()
#Create a rectangle
rect = RectangleF(PointF(0.0, 0.0), SizeF(300.0, 100.0))
#Create a brush with gradient
brush = PdfLinearGradientBrush(rect, PdfRGBColor(Color.get_Red()), PdfRGBColor(Color.get_Blue()), PdfLinearGradientMode.Horizontal)
#Create a true type font with size 20f, underline style
font = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Underline,True)
#Draw text
page.Canvas.DrawString("Welcome to E-iceblue!", font, brush, PointF(0.0, 100.0))
```

---

# Spire.PDF Python Extract Highlighted Text
## Extract highlighted text from a PDF document
```python
# Create a pdf document
doc = PdfDocument()

# Get the first page
page = doc.Pages[0]
textMarkupAnnotation = None

stringBuilder = "Extracted hightlighted text:" + '\n'
# Get the annotation Collection from the document.
annotations = page.AnnotationsWidget

# Update free text annotation.
if annotations.Count > 0:
    for i in range(annotations.Count):
        textMarkupAnnotation = annotations.get_Item(i)
        if isinstance(textMarkupAnnotation, PdfTextMarkupAnnotationWidget):
            # Get the highlighted text
            pdfTextExtractor=PdfTextExtractor(page)
            pdfTextExtractOptions=PdfTextExtractOptions()
            pdfTextExtractOptions.ExtractArea=textMarkupAnnotation.Bounds
            stringBuilder+=pdfTextExtractor.ExtractText(pdfTextExtractOptions)+ '\n'
            # Get the highlighted color
            color = textMarkupAnnotation.TextMarkupColor
```

---

# Spire.PDF Text Extraction
## Extract text from a specific page of a PDF document
```python
# Create a pdf document
doc = PdfDocument()
# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page
page = doc.Pages[0]

# Extract text from page keeping white space
textExtractor = PdfTextExtractor(page)
option = PdfTextExtractOptions()
text = textExtractor.ExtractText(option)

doc.Close()
```

---

# Spire.PDF Text Extraction
## Extract text from a specific rectangular area in a PDF page
```python
# Extract text from a specific rectangular area within the page
pdfTextExtractor=PdfTextExtractor(page)
pdfTextExtractOptions=PdfTextExtractOptions()
pdfTextExtractOptions.ExtractArea=RectangleF(80.0, 180.0, 500.0, 200.0)
text=pdfTextExtractor.ExtractText(pdfTextExtractOptions)
```

---

# Spire.PDF text finding and highlighting
## Find and highlight specific text in PDF pages
```python
# Create PDF document
pdf = PdfDocument()

# Iterate through each page in the PDF
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)

    # Create a PdfTextFinder object for the current page
    finds = PdfTextFinder(page)

    # Set the search parameter to find exact matches
    finds.Options.Parameter = TextFindParameter.none

    # Find instances of the word "science" on the page
    result = finds.Find("science")

    # Iterate through each instance of the word "science" found on the page
    for find in result:
        # Highlight the searched text
        find.HighLight()
```

---

# Spire.PDF text search
## Find and highlight text in a defined area of a PDF document
```python
# Define a rectangle to specify the search area
rctg = RectangleF(0.0, 0.0, 300.0, 300.0)

# Get the first page of the document
pdfPageBase = doc.Pages.get_Item(0)

# Create a PdfTextFinder object for the page
finds = PdfTextFinder(pdfPageBase)

# Set the search parameter to find whole word matches
finds.Options.Parameter = TextFindParameter.WholeWord

# Set the search area to the defined rectangle
finds.Options.Area = rctg

# Find instances of the word "Spire" within the specified rectangle
result = finds.Find("Spire")

# Highlight the found text in green
for find in result:
    find.HighLight(Color.get_Green())

# Find instances of the word "PDF" within the specified rectangle
result2 = finds.Find("PDF")

# Highlight the found text in yellow
for find in result2:
    find.HighLight(Color.get_Yellow())
```

---

# Spire.PDF Font Handling
## Demonstrates various font types and text rendering in PDF documents
```python
# Standard PDF Fonts
# Create a gradient brush for text
l = page.Canvas.ClientSize.Width / float(2)
center = PointF(l, l)
r = float(2 * l * l)
brush = PdfRadialGradientBrush(center, 0.0, center, r, PdfRGBColor(Color.get_Blue()),PdfRGBColor(Color.get_Red()))
y = 200
i = 0

# Compare different font families
text = "Font Family: Helvetica"
x1 = 40.0
y =200.0 + i * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.Helvetica, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)

text = "Font Family: TimesRoman"
x1 = 40.0
y =200.0 + (i := i + 1) * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.TimesRoman, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)

text = "Font Family: Symbol"
x1 = 40.0
y =200.0 + (i := i + 1) * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.Symbol, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)

text = "Font Family: ZapfDingbats"
x1 = 40.0
y =200.0 + (i := i + 1) * 16
font1 = PdfFont(PdfFontFamily.Courier, 14.0)
font2 = PdfFont(PdfFontFamily.ZapfDingbats, 14.0)
x2 = x1 + 10 + font1.MeasureString(text).Width
page.Canvas.DrawString(text, font1, brush, x1, y)
page.Canvas.DrawString(text, font2, brush, x2, y)

# TrueType Fonts
# Embedded TrueType font
trueTypeFont = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)
page.Canvas.DrawString("Font Family: Arial - Embedded", trueTypeFont, brush, 40.0, (y := y + 26.0))

# Non-embedded TrueType font
trueTypeFont = PdfTrueTypeFont("Batang", 14.0, PdfFontStyle.Italic, True)
page.Canvas.DrawString("Font Family: Batang - Not Embedded", trueTypeFont, brush, 40.0, (y := y + 16.0))

# Load font from file
trueTypeFont = PdfTrueTypeFont(inputFontFile, 20.0)
page.Canvas.DrawString("PT Serif Caption Font", trueTypeFont, brush, 40.0, (y := y + 36.0))
page.Canvas.DrawString("PT Serif Caption Font", PdfFont(PdfFontFamily.Helvetica, 8.0), brush, 40.0, (y := y + 40.0))

# Right-to-Left Text
arabicText = "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0628\u062F\u0648\u0631\u0647\u0020\u062D\u0648\u0644\u0647\u0627\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021\u0020" + "\u0627\u0644\u0630\u0647\u0627\u0628\u0021"
trueTypeFont = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)
rctg = RectangleF(PointF(40.0, (y := y + 26)), page.Canvas.ClientSize)
strformat = PdfStringFormat(PdfTextAlignment.Right)
strformat.RightToLeft = True
page.Canvas.DrawString(arabicText, trueTypeFont, brush, rctg, strformat)

# CJK Fonts
# Chinese font
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.MonotypeHeiMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Chinese? \u5B57\u4F53", cjkFont, brush, 40.0, (y := y + 36.0))

# Japanese font
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.HanyangSystemsGothicMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Japanese? \u30D5\u30A9\u30F3\u30C8", cjkFont, brush, 40.0, (y := y + 36.0))

# Korean font
cjkFont = PdfCjkStandardFont(PdfCjkFontFamily.HanyangSystemsShinMyeongJoMedium, 14.0)
page.Canvas.DrawString("How to say 'Font' in Korean? \uAE00\uAF34", cjkFont, brush, 40.0, (y := y + 36.0))
```

---

# Spire.PDF Text Search
## Get details of searched text in PDF
```python
# Create PdfTextFinder object to find all matched phrases
finds = PdfTextFinder(page)
finds.Options.Parameter = TextFindParameter.IgnoreCase
result = finds.Find("Spire.PDF for Python")

# Create a list to store the details of the searched text
details = []

for find in result:
    details.append("==================================================================================" + "\n")
    # Append the found text
    details.append("Text: " + find.Text + "\n")
    # Append the size of the found text
    details.append("Size: Width=" + str(find.Sizes[0].Width) + ", Height=" + str(find.Sizes[0].Height) + "\n")
    # Append the position of the found text
    details.append("Position: X=" + str(find.Positions[0].X) + ", Y=" + str(find.Positions[0].Y) + "\n")
    # Append the line that contains the searched text
    details.append("The line that contains the searched text: " + find.LineText + "\n")
```

---

# Spire.PDF Python Get Font of Searched Text
## Extract font information from searched text in a PDF document
```python
# Create a PDF document object
doc = PdfDocument()

# Load the PDF file into the document object
doc.LoadFromFile(inputfile)

# Get the first page of the PDF document
page = doc.Pages.get_Item(0)

# Create a PdfTextFinder object
finder = PdfTextFinder(page)

# Search for all occurrences of the text "Spire.PDF for Python" in the page
fragments = finder.Find("Spire.PDF for Python")

# Iterate over each found text fragment
for fragment in fragments:
    # Get the font name
    fontName = fragment.TextStates[0].FontName
    
    # Get the font size rounded to 2 decimal places
    fontSize = round(fragment.TextStates[0].FontSize, 2)
```

---

# Spire.PDF Text Size Measurement
## Get text dimensions based on different font types
```python
text = "Spire.PDF for Python"
# Create an instance for PdfFont
font1 = PdfFont(PdfFontFamily.TimesRoman, 12.0)
# Get text size based on font name and size
sizeF1 = font1.MeasureString(text)
# Create an instance for PdfTrueTypeFont
font2 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
# Get text size based on font name and size
sizeF2 = font2.MeasureString(text)
```

---

# Spire.PDF Text Replacement
## Replace all searched text in PDF document
```python
# Get the first page of pdf file
page = doc.Pages[0]

# Searches "Spire.PDF for Python" by ignoring case
finds = PdfTextFinder(doc.Pages[0])
finds.Options.Parameter = TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")
newText = "E-iceblue Spire.PDF"

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)

for find in collection:
    # Gets the bound of the found text in page
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)

    page.Canvas.DrawRectangle(PdfBrushes.get_White(), rec)
    # Draws new text as defined font and color
    page.Canvas.DrawString(newText, font, brush, rec)
```

---

# Spire.PDF text replacement
## Replace first searched text in PDF document
```python
# Get the first page of pdf file
page = doc.Pages[0]

# Searches "Spire.PDF for Python" by ignoring case
finds = PdfTextFinder(page)
finds.Options.Parameter = TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")
newText = "Spire.PDF API"

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)

# Gets the bound of the first found text in page
rec = RectangleF(collection[0].Positions[0].X, collection[0].Positions[0].Y, collection[0].Sizes[0].Width, collection[0].Sizes[0].Height)

page.Canvas.DrawRectangle(PdfBrushes.get_White(), rec)

# Draws new text as defined font and color
page.Canvas.DrawString(newText, font, brush, rec)
```

---

# PDF Font Replacement
## Replace fonts in a PDF document with a new font
```python
#Get the fonts used in PDF
fonts = doc.UsedFonts
#Create a new font 
newfont = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Regular ,True)
for font in fonts:
    #Replace the font with new font
    font.Replace(newfont)
```

---

# Spire.PDF Text Replacement
## Replace text in PDF document
```python
# Create a PdfTextReplacer using a page
replacer = PdfTextReplacer(page)
# Set options
options = PdfTextReplaceOptions()        
options.ReplaceType = ReplaceActionType.WholeWord        
replacer.Options = options  
# Replace all texts in this page
replacer.ReplaceAllText("Spire.PDF","E-iceblue")
# Replace the first found word
replacer.ReplaceText("Adobe Acrobat", "PDF editors")
```

---

# PDF Text Search and Hyperlink Addition
## Search for specific text in a PDF document and add hyperlinks to the found text
```python
# Create a pdf document
doc = PdfDocument()

# Read a pdf file
doc.LoadFromFile(inputFile)

# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the matched phrases
finds = PdfTextFinder(page)
finds.Options.Parameter = TextFindParameter.IgnoreCase
collection = finds.Find("e-iceblue")

# hyperlink url
url = "http://www.e-iceblue.com"

for find in collection:
    # Create a PdfUriAnnotation object to add hyperlink for the searched text
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)
    uri = PdfUriAnnotation(rec)
    uri.Uri = url
    uri.Border = PdfAnnotationBorder(1.0)
    uri.Color = PdfRGBColor(Color.get_Blue())
    page.AnnotationsWidget.Add(uri)
```

---

# PDF Text Search and Rectangle Drawing
## Search for specific text in PDF and draw rectangles around found text
```python
# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the matched phrases
finds = PdfTextFinder(page)
finds.Options.Parameter = TextFindParameter.IgnoreCase
collection = finds.Find("Spire.PDF for Python")

for find in collection:
    # Draw a rectangle with red pen
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)
    page.Canvas.DrawRectangle(
        PdfPen(PdfBrushes.get_Red(), 0.9), rec)
```

---

# spire.pdf text search
## search and replace text using regular expressions
```python
# Get the first page of pdf file
page = doc.Pages[0]

# Create PdfTextFindCollection object to find all the phrases matching the regular expression
finds = PdfTextFinder(doc.Pages[0])
finds.Options.Parameter = TextFindParameter.Regex
collection = finds.Find("\\d{4}")

newText = "New Year"

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_DarkBlue()))

# Defines a font
font = PdfTrueTypeFont("Arial", 7.0, PdfFontStyle.Bold, True)
# Defines text horizontal/vertical center format
centerAlign = PdfStringFormat(
    PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

for find in collection:
    # Gets the bound of the found text in page
    rec = RectangleF(find.Positions[0].X, find.Positions[0].Y, find.Sizes[0].Width, find.Sizes[0].Height)

    page.Canvas.DrawRectangle(PdfBrushes.get_GreenYellow(), rec)
    # Draws new text as defined font and color
    page.Canvas.DrawString(newText, font, brush, rec, centerAlign)
```

---

# spire.pdf python text formatting
## set line breaks in pdf text
```python
#Create a pdf document
doc = PdfDocument()
#Create one A4 page
page = doc.Pages.Add(PdfPageSize.A4(), PdfMargins(40.0))
#Create text
text = "Spire.PDF for Python" + "\n" + "A professional PDF library applied to" + " creating, writing, editing, handling and reading PDF files" + " without any external dependencies within python application."
text += "\n\rSpire.PDF for Java" + "\n" + "A PDF Java API that enables developers to read, " + "write, convert and print PDF documents" + "in Java applications without using Adobe Acrobat."
text += "\n\r"
text += "Welcome to evaluate Spire.PDF!"
#Create rectangle with specified dimensions      
rect = RectangleF(50.0, 50.0, page.Size.Width - 150.0, page.Size.Height)
#Draw the text
page.Canvas.DrawString(text, PdfFont(PdfFontFamily.Helvetica, 13.0), PdfSolidBrush(PdfRGBColor(Color.get_Black())), rect)
```

---

# spire.pdf superscript and subscript
## create superscript and subscript text in pdf
```python
def DrawSuperscript(page, text, font, brush):
        x = 120.0
        y = 100.0
        page.Canvas.DrawString(text, font, brush, PointF(x, y))

        #Measure the string
        size = font.MeasureString(text)

        #Set the x coordinate of the superscript text
        x += size.Width

        #Instantiate a PdfStringFormat instance
        strformat = PdfStringFormat()

        #Set format as superscript
        strformat.SubSuperScript = PdfSubSuperScript.SuperScript

        #Draw superscript text with format
        text = "Superscript"
        page.Canvas.DrawString(text, font, brush, PointF(x, y), strformat)

def DrawSubscript(page, text, font, brush):
        x = 120.0
        y = 150.0
        page.Canvas.DrawString(text, font, brush, PointF(x, y))

        #Measure the string
        size = font.MeasureString(text)

        #Set the x coordinate of the superscript text
        x += size.Width

        #Instantiate a PdfStringFormat instance
        strformat = PdfStringFormat()

        #Set format as superscript
        strformat.SubSuperScript = PdfSubSuperScript.SubScript

        #Draw superscript text with format
        text = "SubScript"
        page.Canvas.DrawString(text, font, brush, PointF(x, y), strformat)
```

---

# Spire.PDF Text Layout
## Demonstrates how to layout text in a PDF document with various formatting options

```python
# Create a pdf document
doc = PdfDocument()
# Create one page
page = doc.Pages.Add()
pageWidth = page.Canvas.ClientSize.Width
y = 0.0

# Page header
pen1 = PdfPen(PdfRGBColor(Color.get_LightGray()), 1.0)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_LightGray()))
font1 = PdfTrueTypeFont("Arial", 8.0, PdfFontStyle.Italic, True)
format1 = PdfStringFormat(PdfTextAlignment.Right)
text = "Demo of Spire.Pdf"
page.Canvas.DrawString(text, font1, brush1, pageWidth - 2, y, format1)
size = font1.MeasureString(text, format1)
y = y + size.Height + 1
page.Canvas.DrawLine(pen1, 0.0, y, pageWidth, y)

# Title
y = y + 25
brush2 = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
font2 = PdfTrueTypeFont("Arial", 18.0, PdfFontStyle.Bold, True)
format2 = PdfStringFormat(PdfTextAlignment.Center)
format2.CharacterSpacing = 1
text = "Summary of Science"
page.Canvas.DrawString(text, font2, brush2, pageWidth / 2, y, format2)
size = font2.MeasureString(text, format2)
y = y + size.Height + 16

# Reference content
font3 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
format3 = PdfStringFormat()
format3.ParagraphIndent = font3.Size * 2
format3.MeasureTrailingSpaces = True
format3.LineSpacing = font3.Size * 1.5
text1 = "(All text and picture from "
text2 = "Wikipedia"
text3 = ", the free encyclopedia)"
page.Canvas.DrawString(text1, font3, brush2, 0.0, y, format3)

size = font3.MeasureString(text1, format3)
x1 = size.Width
format3.ParagraphIndent = 0
font4 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Underline, True)
brush3 = PdfBrushes.get_Blue()
page.Canvas.DrawString(text2, font4, brush3, x1, y, format3)
size = font4.MeasureString(text2, format3)
x1 = x1 + size.Width

page.Canvas.DrawString(text3, font3, brush2, x1, y, format3)
y = y + size.Height

# Content
format4 = PdfStringFormat()
text = "Sample text content for layout demonstration"
font5 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
format4.LineSpacing = font5.Size * 1.5
textLayouter = PdfStringLayouter()
# Define the available space for text
availableWidth = pageWidth - 100  # Leave space for image
availableHeight = 400  # Example height
result = textLayouter.Layout(text, font5, format4, SizeF(availableWidth, availableHeight))
if result.ActualSize.Height < availableHeight:
    availableHeight = availableHeight + result.LineHeight
    result = textLayouter.Layout(text, font5, format4, SizeF(availableWidth, availableHeight))
for line in result.Lines:
    page.Canvas.DrawString(line.Text, font5, brush2, 0.0, y, format4)
    y = y + result.LineHeight + 2
textWidget = PdfTextWidget(result.Remainder, font5, brush2)
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
textWidget.StringFormat = format4
textWidget.Draw(page, bounds, textLayout)
```

---

# Spire.PDF Text Wrapping Around Image
## Demonstrates how to wrap text around an image in a PDF document
```python
# Creates a pdf document
doc = PdfDocument()

# Creates a page 
page = doc.Pages.Add()

#Gets page width
pageWidth = page.Canvas.ClientSize.Width
y = 0.0

# Creates a brush
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))

# Defines fonts
font1 = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Bold ,True)
font2 = PdfTrueTypeFont("Arial", 16.0 , PdfFontStyle.Regular, True)

# Defines text formats
format1 = PdfStringFormat(PdfTextAlignment.Center)
format1.CharacterSpacing = 1.0

format2 = PdfStringFormat()
format2.LineSpacing = font2.Size * 1.5

# Draw title text
text = "Spire.PDF for Python"
page.Canvas.DrawString(text, font1, brush, pageWidth / 2, y, format1)
size = font1.MeasureString(text, format1)
y = y + size.Height + 6

# Draw image (assuming image is loaded)
page.Canvas.DrawImage(image, PointF(pageWidth - image.PhysicalDimension.Width, y))
imageLeftSpace = pageWidth - image.PhysicalDimension.Width - 2
imageBottom = image.PhysicalDimension.Height + y

# Layout text around image
textLayouter = PdfStringLayouter()
imageLeftBlockHeight = imageBottom - y
result = textLayouter.Layout(text, font2, format2, SizeF(imageLeftSpace, imageLeftBlockHeight))
if result.ActualSize.Height < imageLeftBlockHeight:
    imageLeftBlockHeight = imageLeftBlockHeight + result.LineHeight
    result = textLayouter.Layout(text, font2, format2, SizeF(imageLeftSpace, imageLeftBlockHeight))

# Draw text lines around image
for line in result.Lines:
    page.Canvas.DrawString(line.Text, font2, brush, 0.0, y, format2)
    y = y + result.LineHeight

# Draw remaining text
textWidget = PdfTextWidget(result.Remainder, font2, brush)
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
textWidget.StringFormat = format2
textWidget.Draw(page, bounds, textLayout)
```

---

# Spire.PDF Python SVG to PDF
## Add SVG content to an existing PDF document
```python
#Create a new PDF document.
existingPDF = PdfDocument()
#Load an existing PDF
existingPDF.LoadFromFile(pdfFile)
#Create a new PDF document.
doc = PdfDocument()
#Load the SVG file
doc.LoadFromSvg(svgFile)
#Create template
template = doc.Pages[0].CreateTemplate()
#Draw template on existing PDF
existingPDF.Pages[0].Canvas.DrawTemplate(doc.Pages[0].CreateTemplate(), PointF(50.0, 350.0), SizeF(200.0, 200.0))
```

---

# Convert PDF pages to EMF images
## Open PDF document and convert all pages to EMF format
```python
# Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToEMF-img-{0:d}.emf".format(i)
    with pdf.SaveAsImage(i,PdfImageType.Bitmap) as imageS:
         imageS.Save(fileName)
pdf.Close()
```

---

# PDF to PNG Conversion
## Convert all pages of a PDF document to PNG images
```python
# Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToPNG-img-{0:d}.png".format(i)
    with pdf.SaveAsImage(i) as imageS:
         imageS.Save(fileName)
pdf.Close()
```

---

# Spire.PDF Image Stream to PDF Conversion
## Convert image stream to PDF document with proper sizing
```python
# Create a pdf document with a section and page added.
pdf = PdfDocument()
section = pdf.Sections.Add()
page = section.Pages.Add()
# Load image from stream
image = PdfImage.FromStream(imageStream)
#Set image display location and size in PDF
#Calculate rate
widthFitRate = image.PhysicalDimension.Width / page.Canvas.ClientSize.Width
heightFitRate = image.PhysicalDimension.Height / page.Canvas.ClientSize.Height
fitRate = max(widthFitRate, heightFitRate)
#Calculate the size of image 
fitWidth = image.PhysicalDimension.Width / fitRate
fitHeight = image.PhysicalDimension.Height / fitRate
#Draw image
page.Canvas.DrawImage(image, 0.0, 30.0, fitWidth, fitHeight)
```

---

# Spire.PDF for Python
## Convert image to PDF
```python
# Create a pdf document with a section and page added.
pdf = PdfDocument()
section = pdf.Sections.Add()
page = pdf.Pages.Add()
#Load an image from system
image = PdfImage.FromFile(inputFile)
#Set image display location and size in PDF
#Calculate rate
widthFitRate = math.trunc(image.PhysicalDimension.Width / float(page.Canvas.ClientSize.Width))
heightFitRate = math.trunc(image.PhysicalDimension.Height / float(page.Canvas.ClientSize.Height))
fitRate = max(widthFitRate, heightFitRate)
#Calculate the size of image 
fitWidth = image.PhysicalDimension.Width / fitRate
fitHeight = image.PhysicalDimension.Height / fitRate
#Draw image
page.Canvas.DrawImage(image, 0.0, 30.0, fitWidth, fitHeight)
pdf.SaveToFile(outputFile)
pdf.Close()
```

---

# PDF to BMP Conversion
## Convert PDF pages to BMP images using Spire.PDF
```python
# Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile("input.pdf")
# Save to images
for i in range(pdf.Pages.Count):
    fileName = "ToBMP-img-{0:d}.bmp".format(i)
    with pdf.SaveAsImage(i) as imageS:
        imageS.Save(fileName)
pdf.Close()
```

---

# Spire.PDF Python Image Deletion
## Delete an image from a PDF document
```python
# Get the first page
page = pdf.Pages[0]

# Create image helper
imageHelper = PdfImageHelper()

# Get a collection of images on one page
imageInfos = imageHelper.GetImagesInfo(page)

# Delete the first image
imageHelper.DeleteImage(imageInfos[0])
```

---

# Spire.PDF Delete Images by Bounds
## Delete images from PDF based on their bounds or position
```python
# Get the first page
page = pdf.Pages[0]
# Get image helper
imageHelper = PdfImageHelper()
# Get image information from the page
imageInfo = imageHelper.GetImagesInfo(page)
# Iterate through all images
for i in range(len(imageInfo)):
    # Delete image if its bounds contain the specified point
    if imageInfo[i].Bounds.Contains(49.68, 73.1):
        imageHelper.DeleteImage(imageInfo[i])
    # Delete image if its bounds intersect with the specified rectangle
    if imageInfo[i].Bounds.IntersectsWith(RectangleF(100.0, 500.0, 30.0, 40.0)):
        imageHelper.DeleteImage(imageInfo[i])
```

---

# spire.pdf delete image
## delete the first image from a pdf page
```python
#Get the first page
page = pdf.Pages[0]
#Delete the first image on the page
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
imageHelper.DeleteImage(imageInfo[0])
```

---

# spire.pdf python delete image
## delete image from pdf page using PdfImageHelper
```python
#Delete the first image on the page
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
imageHelper.DeleteImage(imageInfo[0])
```

---

# Spire.PDF Python Image Drawing
## Draw and transform images in a PDF document
```python
# Create a PDF document and page
doc = PdfDocument()
page = doc.Pages.Add()

# Drawing text with transformations
state = page.Canvas.Save()
font = PdfFont(PdfFontFamily.Helvetica, 18.0)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
brush2 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
strformat = PdfStringFormat(PdfTextAlignment.Center)
page.Canvas.TranslateTransform(math.trunc(page.Canvas.ClientSize.Width / float(2)), 20.0)
page.Canvas.DrawString("Chart image", font, brush1, 0.0, 0.0, strformat)
page.Canvas.ScaleTransform(1, -0.8)
page.Canvas.DrawString("Chart image", font, brush2, 0.0, -2 * 18 * 1.2, strformat)
page.Canvas.Restore(state)

# Load and draw an image
image = PdfImage.FromFile("path/to/image.png")
width = image.Width * 0.75
height = image.Height * 0.75
x = (page.Canvas.ClientSize.Width - width) / 2
page.Canvas.DrawImage(image, x, 60.0, width, height)

# Create a transformed template and draw with transparency
skewX = 20.0
skewY = 20.0
scaleX = 0.2
scaleY = 0.6
width = float(((image.Width + image.Height * math.tan(math.pi * skewX/ 180)) * scaleX))
height = float(((image.Height + image.Width * math.tan(math.pi * skewY/ 180)) * scaleY))
template = PdfTemplate(width, height)
template.Graphics.ScaleTransform(scaleX, scaleY)
template.Graphics.SkewTransform(skewX, skewY)
template.Graphics.DrawImage(image, 0.0, 0.0)
state = page.Canvas.Save()
page.Canvas.TranslateTransform(page.Canvas.ClientSize.Width - 50, 260.0)
offset = math.trunc((page.Canvas.ClientSize.Width - 100) / float(12))
for i in range(0, 12):
    page.Canvas.TranslateTransform(-offset, 0.0)
    page.Canvas.SetTransparency(i / 12.0)
    page.Canvas.DrawTemplate(template, PointF(0.0, 0.0))
page.Canvas.Restore(state)
```

---

# Spire.PDF image extraction
## Extract images from PDF as byte arrays
```python
# Create a PDF document object
doc = PdfDocument()

# Load the PDF file into the document object
doc.LoadFromFile(inputfile)

# Get the first page of the PDF document
page = doc.Pages.get_Item(0)

# Retrieve the information about images on the page
imageInfo = page.ImagesInfo

# Iterate over all images found on the page
for i in range(len(imageInfo)):
    # Convert the image to a byte array
    byteResult = imageInfo[i].Image.ToArray()
```

---

# PDF to EMF Conversion
## Convert a PDF page to EMF image format
```python
# Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
# Save to images
with pdf.SaveAsImage(1) as imageS:
    imageS.Save(outputFile)
pdf.Close()
```

---

# Spire.PDF Page to PNG Conversion
## Convert a PDF page to PNG image format

```python
# Open pdf document
pdf = PdfDocument()
pdf.LoadFromFile(inputfile)
# Save PDF page to PNG
with pdf.SaveAsImage(1) as imageS:
    imageS.Save(outputFile)
pdf.Close()
```

---

# Spire.PDF Image Replacement
## Replace an image in a PDF document using the first approach
```python
#Get the first page.
page = doc.Pages[0]
#Get images of the first page.
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
#Replace the first image on the page.
newImage = PdfImage.FromFile("path_to_image")
imageHelper.ReplaceImage(imageInfo[0], newImage)
```

---

# PDF image replacement
## Replace an image in a PDF document using PdfImageHelper
```python
# Create an image helper
imageHelper = PdfImageHelper()
# Get image information from a page
imageInfo = imageHelper.GetImagesInfo(page)
# Replace the first image with a new image
imageHelper.ReplaceImage(imageInfo[0], PdfImage.FromFile("path_to_image"))
```

---

# spire.pdf image replacement
## replace image with text in pdf
```python
#Get the first page.
page = doc.Pages[0]
#Get images of the first page.
imageHelper = PdfImageHelper()
imageInfo = imageHelper.GetImagesInfo(page)
image = PdfImage.FromStream(imageInfo[0].Image)
#Get width and height of image
widthInPixel = image.Width
heightInPixel = image.Height
#Convert unit from Pixel to Point
convertor = PdfUnitConvertor()
width = convertor.ConvertFromPixels(float(widthInPixel), PdfGraphicsUnit.Point)
height = convertor.ConvertFromPixels(float(heightInPixel), PdfGraphicsUnit.Point)
#Get location of image
xPos = imageInfo[0].Bounds.X
yPos = imageInfo[0].Bounds.Y
#Remove the image
imageHelper.DeleteImage(imageInfo[0])
#Define a rectangle
rect = RectangleF(PointF(xPos, yPos), SizeF(width, height))
#Define string format
strformat = PdfStringFormat()
strformat.Alignment= PdfTextAlignment.Center
strformat.LineAlignment= PdfVerticalAlignment.Middle
#Draw a string at the location of the image
page.Canvas.DrawString("ReplacedText", PdfFont(PdfFontFamily.Helvetica, 18.0), PdfBrushes.get_Purple(), rect, strformat)
```

---

# Spire.PDF Python Image Size Control
## Set image size and position in PDF document
```python
# Create a pdf document
doc = PdfDocument()

# Create one page
page = doc.Pages.Add()

# Load an image
image = PdfImage.FromFile("image_path")

# Set the width and height of image
width = image.Width * 0.75
height = image.Height * 0.75

# Define a position to draw image
x = (page.Canvas.ClientSize.Width - width) / 2
y = 60.0

# Draw image on page canvas
page.Canvas.DrawImage(image, x, y, width, height)
```

---

# Spire.PDF Python List with Custom Marker
## Create a PDF list with custom image markers
```python
# Create a new PdfDocument
doc = PdfDocument()

# Add a new page to the document
page = doc.Pages.Add()

# Create a PdfMarker object with a custom image marker style
marker = PdfMarker(PdfUnorderedMarkerStyle.CustomImage)

# Set the image for the marker
marker.Image = PdfImage.FromFile(inputFile_Img)

# Define the content for the list
listContent = "Data Structure\n"
listContent += "Algorithm\n"
listContent += "Computer Networks\n"
listContent += "Operating System\n"
listContent += "C Programming\n"
listContent += "Computer Organization and Architecture"

# Create a PdfList object with the specified content
list = PdfList(listContent)

# Set the indentation for the list
list.Indent = 2

# Set the text indentation for the list
list.TextIndent = 4

# Set the marker for the list using the custom image marker
list.Marker = marker

# Draw the list on the page at the specified coordinates
list.Draw(page.Canvas, 100, 100)
```

---

# Spire.PDF Barcode Generation
## Create and draw various types of barcodes in a PDF document
```python
# Draw Codabar
text = PdfTextWidget()
text.Font = font1
text.Text = "Codabar:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode1 = PdfCodabarBarcode("00:12-3456/7890")
barcode1.BarcodeToTextGapHeight = 1.0
barcode1.EnableCheckDigit = True
barcode1.ShowCheckDigit = True
barcode1.TextDisplayLocation = TextLocation.Bottom
barcode1.TextColor = PdfRGBColor(Color.get_Blue())
barcode1.Draw(page, PointF(0.0, y))
y = barcode1.Bounds.Bottom + 5

# Draw Code11Barcode
text.Text = "Code11:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode2 = PdfCode11Barcode("123-4567890")
barcode2.BarcodeToTextGapHeight = 1.0
barcode2.TextDisplayLocation = TextLocation.Bottom
barcode2.TextColor = PdfRGBColor(Color.get_Blue())
barcode2.Draw(page, PointF(0.0, y))
y = barcode2.Bounds.Bottom + 5

# Draw Code32
text.Text = "Code32:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode5 = PdfCode32Barcode("16273849")
barcode5.BarcodeToTextGapHeight = 1.0
barcode5.TextDisplayLocation = TextLocation.Bottom
barcode5.TextColor = PdfRGBColor(Color.get_Blue())
barcode5.Draw(page, PointF(0.0, y))
y = barcode5.Bounds.Bottom + 5

# Draw Code39
text.Text = "Code39:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode6 = PdfCode39Barcode("16-273849")
barcode6.BarcodeToTextGapHeight = 1.0
barcode6.TextDisplayLocation = TextLocation.Bottom
barcode6.TextColor = PdfRGBColor(Color.get_Blue())
barcode6.Draw(page, PointF(0.0, y))
y = barcode6.Bounds.Bottom + 5

# Draw Code39-E
text.Text = "Code39-E:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode7 = PdfCode39ExtendedBarcode("16-273849")
barcode7.BarcodeToTextGapHeight = 1.0
barcode7.TextDisplayLocation = TextLocation.Bottom
barcode7.TextColor = PdfRGBColor(Color.get_Blue())
barcode7.Draw(page, PointF(0.0, y))
y = barcode7.Bounds.Bottom + 5

# Draw Code93
text.Text = "Code93:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode8 = PdfCode93Barcode("16-273849")
barcode8.BarcodeToTextGapHeight = 1.0
barcode8.TextDisplayLocation = TextLocation.Bottom
barcode8.TextColor = PdfRGBColor(Color.get_Blue())
barcode8.QuietZone.Bottom = 5.0
barcode8.Draw(page, PointF(0.0, y))
y = barcode8.Bounds.Bottom + 5

# Draw Code93-E
text.Text = "Code93-E:"
result = text.Draw(page, 0.0, y)
page = result.Page
y = result.Bounds.Bottom + 2
barcode9 = PdfCode93ExtendedBarcode("16-273849")
barcode9.BarcodeToTextGapHeight = 1.0
barcode9.TextDisplayLocation = TextLocation.Bottom
barcode9.TextColor = PdfRGBColor(Color.get_Blue())
barcode9.Draw(page, PointF(0.0, y))
y = barcode9.Bounds.Bottom + 5
```

---

# spire.pdf spot color drawing
## drawing content with spot color in pdf
```python
#Get the first page
page = pdf.Pages[0]
#Initialize an instance of PdfSeparationColorSpace
cs = PdfSeparationColorSpace("MySpotColor", PdfRGBColor(Color.get_DarkViolet()))
#Set tini = 1 for the cs
color = PdfSeparationColor(cs, 1.0)
#Create a brush with spot color
brush = PdfSolidBrush(color)
#Draw a string
page.Canvas.DrawString("Tint=1.0", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(160.0, 160.0))
#Draw pie with spot color(DarkViolet)
page.Canvas.DrawPie(brush, 148.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.7", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(230.0, 160.0))
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.4", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(300.0, 160.0))
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 200.0, 60.0, 60.0, 360.0, 360.0)
page.Canvas.DrawString("Tint=0.1", PdfFont(PdfFontFamily.Helvetica, 10.0), brush, PointF(370.0, 160.0))
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 200.0, 60.0, 60.0, 360.0, 360.0)
#Draw pie with spot color(Purple)
cs = PdfSeparationColorSpace("MySpotColor",PdfRGBColor(Color.get_Purple()))
color = PdfSeparationColor(cs, 1.0)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 148.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 280.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 280.0, 60.0, 60.0, 360.0, 360.0)
#Draw pie with spot color(DarkSlateBlue)
cs = PdfSeparationColorSpace("MySpotColor",PdfRGBColor(Color.get_DarkSlateBlue()))
color = PdfSeparationColor(cs, 1.0)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 148.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.7)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 218.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.4)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 288.0, 360.0, 60.0, 60.0, 360.0, 360.0)
color = PdfSeparationColor(cs, 0.1)
brush = PdfSolidBrush(color)
page.Canvas.DrawPie(brush, 358.0, 360.0, 60.0, 60.0, 360.0, 360.0)
```

---

# Spire.PDF Python Drawing Dashed Line
## Demonstrates how to draw a dashed line on a PDF page
```python
#Save graphics state
state = page.Canvas.Save()
#Set location and size
x = 150.0
y = 200.0
width = 300.0
#Create pens
pen = PdfPen(PdfRGBColor(Color.get_Red()), 3.0)
#Set dash style and pattern
pen.DashStyle = PdfDashStyle.Dash
pen.DashPattern = [1, 4, 1]
#Draw dashed line
page.Canvas.DrawLine(pen, x, y, x + width, y)
#Restore graphics
page.Canvas.Restore(state)
```

---

# Drawing Filled Rectangles in PDF
## This code demonstrates how to draw a filled rectangle on a PDF page using Spire.PDF for Python.
```python
# Save graphics state
state = page.Canvas.Save()
# Set rectangle display location and size
x = 200.0
y = 300.0
width = 200.0
height = 120.0
# Create pen and brush
pen = PdfPen(PdfRGBColor(Color.get_Black()), 1.0)
brush = PdfSolidBrush(PdfRGBColor(Color.get_OrangeRed()))
# Draw a filled rectangle
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
# Restore graphics
page.Canvas.Restore(state)
```

---

# spire.pdf python drawing lines
## Draw lines and shapes in a PDF document
```python
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw line
#Set location and size
x = 95.0
y = 95.0
width = 400.0
height = 500.0
#Create pens
pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.1)
pen1 = PdfPen(PdfRGBColor(Color.get_Red()), 0.1)
#Draw a rectangle
page.Canvas.DrawRectangle(pen, x, y, width, height)
#Draw two crossed lines
page.Canvas.DrawLine(pen1, x, y, x + width, y + height)
page.Canvas.DrawLine(pen1, x + width, y, x, y + height)
#Restore graphics
page.Canvas.Restore(state)
```

---

# Drawing Rectangles on PDF
## Core functionality to draw rectangles with different styles on a PDF page
```python
# Save graphics state
state = page.Canvas.Save()
# Draw rectangles
# Set rectangle display location and size
x = 130.0
y = 100.0
width = 400.0
height = 400.0
# Create pen for rectangle
pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.1)
page.Canvas.DrawRectangle(pen, RectangleF(PointF(x, y), SizeF(width, height)))
# Draw second rectangle with different size and style
y = y + height - 50
width = 100.0
height = 50.0
# Initialize an instance of PdfSeparationColorSpace
cs = PdfSeparationColorSpace("MyColor", PdfRGBColor(Color.FromArgb(0, 100, 0, 0)))
pen1 = PdfPen(PdfRGBColor(Color.get_Red()), 1.0)
# Create a brush with spot color
brush = PdfSolidBrush(PdfSeparationColor(cs, 0.1))
page.Canvas.DrawRectangle(pen1, brush, RectangleF(PointF(x, y), SizeF(width, height)))
# Restore graphics
page.Canvas.Restore(state)
```

---

# Drawing Shapes in PDF with Spire.PDF
## Demonstrates how to draw various shapes in a PDF document including paths with different fill modes, Spiro curves, rectangles, pies, and ellipses

```python
# Draw path with different fill modes
points = [None]*5
i = 0
while i < 5:
    x = float(math.cos(i * 2 * math.pi / 5))
    y = float(math.sin(i * 2 * math.pi / 5))
    points[i] = PointF(x, y)
    i += 1
path = PdfPath()
path.AddLine(points[2], points[0])
path.AddLine(points[0], points[3])
path.AddLine(points[3], points[1])
path.AddLine(points[1], points[4])
path.AddLine(points[4], points[2])
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_DeepSkyBlue()), 0.02)
brush1 = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
page.Canvas.ScaleTransform(50.0, 50.0)
page.Canvas.TranslateTransform(5.0, 1.2)
page.Canvas.DrawPath(pen, path)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Alternate
page.Canvas.DrawPath(pen, brush1, path)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush1, path)
brush2 = PdfLinearGradientBrush(PointF(-2.0, 0.0), PointF(2.0, 0.0), PdfRGBColor(Color.get_Red()), PdfRGBColor(Color.get_Blue()))
page.Canvas.TranslateTransform(-4.0, 2.0)
path.FillMode = PdfFillMode.Alternate
page.Canvas.DrawPath(pen, brush2, path)
brush3 = PdfRadialGradientBrush(PointF(0.0, 0.0), 0.0, PointF(0.0, 0.0), 1.0, PdfRGBColor(Color.get_Red()) , PdfRGBColor(Color.get_Blue()))
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush3, path)
brush4 = PdfTilingBrush(RectangleF(0.0, 0.0, 4.0, 4.0))
brush4.Graphics.DrawRectangle(brush2, 0.0, 0.0, 4.0, 4.0)
page.Canvas.TranslateTransform(2.0, 0.0)
path.FillMode = PdfFillMode.Winding
page.Canvas.DrawPath(pen, brush4, path)
page.Canvas.Restore(state)

# Draw Spiro shape
state = page.Canvas.Save()
pen = PdfPens.get_DeepSkyBlue()
nPoints = 1000
r1 = 30
r2 = 25
p = 35
x1 = r1 + r2 - p
y1 = 0
x2 = 0
y2 = 0
page.Canvas.TranslateTransform(100.0, 100.0)
for i in range(0, nPoints):
    t = i * math.pi / 90
    x2 = (r1 + r2) * math.cos(t) - p * math.cos((r1 + r2) * t / r2)
    y2 = (r1 + r2) * math.sin(t) - p * math.sin((r1 + r2) * t / r2)
    page.Canvas.DrawLine(pen, float(x1), float(y1), float(x2), float(y2))
    x1 = x2
    y1 = y2
page.Canvas.Restore(state)

# Draw rectangle
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_Chocolate()) , 1.0)
page.Canvas.DrawRectangle(pen, RectangleF(PointF(20.0, 310.0), SizeF(150.0, 120.0)))
page.Canvas.Restore(state)

# Draw pie
state = page.Canvas.Save()
pen = PdfPen(PdfRGBColor(Color.get_DarkRed()), 2.0)
page.Canvas.DrawPie(pen, 220.0, 320.0, 100.0, 90.0, 360.0, 360.0)
page.Canvas.Restore(state)

# Draw ellipse
state = page.Canvas.Save()
brush = PdfSolidBrush(PdfRGBColor(Color.get_CadetBlue()))
page.Canvas.DrawEllipse(brush, 380.0, 325.0, 80.0, 80.0)
page.Canvas.Restore(state)
```

---

# Spire.PDF List Creation
## Create different types of lists in PDF document
```python
# Common list data and styling
listData = "Beverages\nCondiments\nConfections\nDairy Products\nGrains/Cereals\nMeat/Poultry\nProduce\nSeafood"
font = PdfFont(PdfFontFamily.Helvetica, 12.0, PdfFontStyle.Bold)
brush = PdfLinearGradientBrush(RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize), 
                              PdfRGBColor(Color.get_Navy()), 
                              PdfRGBColor(Color.get_OrangeRed()), 
                              PdfLinearGradientMode.Vertical)

# Create a basic list
basicList = PdfList(listData)
basicList.Font = font
basicList.Indent = 8
basicList.TextIndent = 5
basicList.Brush = brush
PdfLayoutWidget(basicList).Draw(page, 0.0, y)

# Create a sorted list
sortedList = PdfSortedList(listData)
sortedList.Font = font
sortedList.Indent = 8
sortedList.TextIndent = 5
sortedList.Brush = brush
PdfLayoutWidget(sortedList).Draw(page, 0.0, y)

# Create a sorted list with Roman numeral markers
romanList = PdfSortedList(listData)
romanList.Font = font
romanList.Marker = PdfOrderedMarker(PdfNumberStyle.LowerRoman, PdfFont(PdfFontFamily.Helvetica, 12.0))
romanList.Indent = 8.0
romanList.TextIndent = 5.0
romanList.Brush = brush
PdfLayoutWidget(romanList).Draw(page, 0.0, y)

# Create a sorted list with Latin letter markers
latinList = PdfSortedList(listData)
latinList.Font = font
latinList.Marker = PdfOrderedMarker(PdfNumberStyle.LowerLatin, PdfFont(PdfFontFamily.Helvetica, 12.0))
latinList.Indent = 8.0
latinList.TextIndent = 5.0
latinList.Brush = brush
PdfLayoutWidget(latinList).Draw(page, 0.0, y)
```

---

# PDF Overlay
## Overlay one PDF document onto another with transparency
```python
#Create page template from the first document
template = doc1.Pages[0].CreateTemplate()
#Overlay the template onto each page of the second document
for i in range(doc2.Pages.Count):
    page = doc2.Pages.get_Item(i)
    page.Canvas.SetTransparency(0.25,0.25, PdfBlendMode.Overlay)
    page.Canvas.DrawTemplate(template, PointF.Empty())
```

---

# Set Rectangle Transparency in PDF
## This code demonstrates how to draw rectangles with different transparency levels in a PDF document
```python
#Create one page
page = pdf.Pages[0]
#Save graphics state
state = page.Canvas.Save()
#Draw rectangles
x = 200.0
y = 300.0
width = 200.0
height = 100.0
pen = PdfPen(PdfRGBColor(Color.get_Black()), 1.0)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Red()))
page.Canvas.SetTransparency(0.5, 0.5)
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
x = x + int(width / 2.0)
y = y - int(height / 2.0)
page.Canvas.SetTransparency(0.2, 0.2)
page.Canvas.DrawRectangle(pen, brush, RectangleF(PointF(x, y), SizeF(width, height)))
#Restore graphics
page.Canvas.Restore(state)
```

---

# PDF Transparency Blend Modes
## Create PDF with different transparency blend modes
```python
#Create a pdf document
doc = PdfDocument()
#Create one section
section = doc.Sections.Add()

#for mode in Enum.GetValues(type_of(PdfBlendMode)):
for mode in PdfBlendMode.__members__:
    page = section.Pages.Add()
    pageWidth = page.Canvas.ClientSize.Width
    y = 0.0
    #Title
    y = y + 15
    brush = PdfSolidBrush(PdfRGBColor(Color.get_OrangeRed()))
    font = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold,True)
    format = PdfStringFormat(PdfTextAlignment.Center)
    text = "Transparency Blend Mode: {0:s}".format(mode)
    page.Canvas.DrawString(text, font, brush, pageWidth / 2, y, format)
    size = font.MeasureString(text, format)
    y = y + size.Height + 25
    page.Canvas.DrawImage(image, 0.0, y, imageWidth, imageHeight)
    page.Canvas.Save()
    d = (page.Canvas.ClientSize.Width - imageWidth) / 5
    x = d
    y = y + d / 2+40
    for i in range(0, 5):
        alpha = 1.0 / 6 * (5 - i)
        page.Canvas.SetTransparency(alpha, alpha, PdfBlendMode[mode])
        page.Canvas.DrawImage(image, x, y, imageWidth, imageHeight)
        x = x + d
        y = y + d / 2+ 40
    page.Canvas.Restore()
```

---

# Spire.PDF Python Free Text Annotation
## Add free text annotations to PDF documents
```python
#Add free text annotation
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\n  Spire.PDF"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.TimesRoman, 20.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Gray())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Slash
textAnnotation.Color = PdfRGBColor(Color.get_LightBlue())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
```

---

# Spire.PDF Annotations
## Create various types of annotations in PDF document
```python
# Create a pdf document
doc = PdfDocument()
# Margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
# Title
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle['Bold'].value | PdfFontStyle['Italic'].value, True)
format1 = PdfStringFormat(PdfTextAlignment.Left)
y = 50.0
s = "The sample demonstrates how to add annotations in PDF document."
page.Canvas.DrawString(s, font1, brush1, 0.0, y-5, format1)
y = y + font1.MeasureString(s, format1).Height
y = y + 15
newPage = PdfNewPage(page.Ptr)

# Document Link Annotation
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Document Link: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
dest = PdfDestination(page)
dest.Mode = PdfDestinationMode.Location
dest.Location = PointF(0.0, y)
dest.Zoom = 2.0
label = "Click me, Zoom 200%"
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
annotation = PdfDocumentLinkAnnotation(bounds, dest)
annotation.Color = PdfRGBColor(Color.get_Blue())
newPage.Annotations.Add(annotation)
y = bounds.Bottom

# File Link Annotation
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Launch File: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """Launch Notepad.exe"""
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
annotation = PdfFileLinkAnnotation(bounds, "C:\\Windows\\Notepad.exe")
annotation.Color = PdfRGBColor(Color.get_Blue())
newPage.Annotations.Add(annotation)
y = bounds.Bottom

# Free Text Annotation
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Text Markup: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """I'm a text box, not a TV"""
size = font.MeasureString(label)
bounds = RectangleF(x, y, size.Width, size.Height)
page.Canvas.DrawRectangle(PdfPen(PdfRGBColor(Color.get_Blue()), 0.1), bounds)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
location = PointF(bounds.Right + 16, bounds.Top - 16)
annotaionBounds = RectangleF(location, SizeF(80.0, 32.0))
annotation = PdfFreeTextAnnotation(annotaionBounds)
annotation.AnnotationIntent = PdfAnnotationIntent.FreeTextCallout
annotation.Border = PdfAnnotationBorder(0.5)
annotation.BorderColor = PdfRGBColor(Color.get_Red())
location = PointF(bounds.Right + 16, bounds.Top - 16)
annotation.CalloutLines = [PointF(bounds.Right, bounds.Top), PointF(bounds.Right+8, bounds.Top - 8), location]
annotation.Color = PdfRGBColor(Color.get_Yellow())
annotation.Flags = PdfAnnotationFlags.Locked
annotation.Font = font
annotation.LineEndingStyle = PdfLineEndingStyle.OpenArrow
annotation.MarkupText = "Just a joke."
annotation.Opacity = 0.75
annotation.TextMarkupColor =PdfRGBColor(Color.get_Green())
newPage.Annotations.Add(annotation)
y = bounds.Bottom

# Line Annotation
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Line Annotation: "
size = font.MeasureString(prompt)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = font.MeasureString(prompt, format).Width
label = """Line Anotation"""
size = font.MeasureString(label)
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
bounds = RectangleF(x, y, size.Width, size.Height)
linePoints = [int(bounds.Left), int(bounds.Top), int(bounds.Right), int(bounds.Bottom)]
annotation = PdfLineAnnotation(linePoints, "Annotation")
annotation.BeginLineStyle = PdfLineEndingStyle.ClosedArrow
annotation.EndLineStyle = PdfLineEndingStyle.ClosedArrow
annotation.LineCaption = True
annotation.BackColor = PdfRGBColor(Color.get_Black())
annotation.CaptionType = PdfLineCaptionType.Inline
newPage.Annotations.Add(annotation)
y = bounds.Bottom

# Text Markup Annotation (Highlight)
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Highlight incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of anotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
size = font.MeasureString("demo of ", format)
x = x + size.Width
incorrectWordLocation = PointF(x, y)
markupText = "Should be 'annotation'"
annotation = PdfTextMarkupAnnotation(markupText, "anotation",RectangleF(x, y, 100.0, 100.0), font)
annotation.TextMarkupAnnotationType = PdfTextMarkupAnnotationType.Highlight
annotation.TextMarkupColor = PdfRGBColor(Color.get_LightSkyBlue())
newPage.Annotations.Add(annotation)
y = y + size.Height

# Popup Annotation
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Markup incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of annotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
x = x + font.MeasureString(label, format).Width
markupText = "All words were spelled correctly"
size = font.MeasureString(markupText)
annotation = PdfPopupAnnotation(RectangleF(PointF(x, y), SizeF.Empty()), markupText)
annotation.Icon = PdfPopupIcon.Paragraph
annotation.Open = True
annotation.Color = PdfRGBColor(Color.get_Yellow())
newPage.Annotations.Add(annotation)
y = y + size.Height

# Rubber Stamp Annotation
y = y + 6
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular,True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True
prompt = "Markup incorrect spelling: "
size = font.MeasureString(prompt, format)
page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
x = size.Width
label = "demo of annotation"
page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
x = x + font.MeasureString(label, format).Width
markupText = "Just a draft, not checked."
size = font.MeasureString(markupText)
annotation = PdfRubberStampAnnotation(RectangleF(x, y, font.Height, font.Height), markupText)
annotation.Icon = PdfRubberStampAnnotationIcon.Draft
annotation.Color = PdfRGBColor(Color.get_Plum())
newPage.Annotations.Add(annotation)
y = y + size.Height
```

---

# Spire.PDF 3D Annotation Creation
## Create a 3D annotation in a PDF document
```python
#Create a new Pdf document.
doc = PdfDocument()
#Add a new page to it.
page = doc.Pages.Add()
#Draw a rectangle on the page to define the canvas area for the 3D file.
rt = RectangleF(0.0, 80.0, 200.0, 200.0)
#Initialize a new object of Pdf3DAnnotation, load the .u3d file as 3D annotation.
annotation = Pdf3DAnnotation(rt, "path_to_3d_file.u3d")
annotation.Activation = Pdf3DActivation()
annotation.Activation.ActivationMode = Pdf3DActivationMode.PageOpen
#Define a 3D view mode.
View = Pdf3DView()
View.Background = Pdf3DBackground(PdfRGBColor(Color.get_Purple()))
View.ViewNodeName = "3DAnnotation"
View.RenderMode = Pdf3DRendermode(Pdf3DRenderStyle.Solid)
View.InternalName = "3DAnnotation"
View.LightingScheme = Pdf3DLighting()
View.LightingScheme.Style = Pdf3DLightingStyle.Day
#Set the 3D view mode for the annotation.
annotation.Views.Add(View)
#Add the annotation to Pdf.
page.AnnotationsWidget.Add(annotation)
```

---

# Spire.PDF Python Line Annotation
## Create and configure PDF line annotations with different styles
```python
# Create a line annotation
linePoints = [100, 650, 180, 650]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the first line annotation")
# Set the line border
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Solid
lineAnnotation.lineBorder.BorderWidth = 1
# Set the line intent
lineAnnotation.LineIntent = PdfLineIntent.LineDimension
# Set the line style
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.Butt
lineAnnotation.EndLineStyle = PdfLineEndingStyle.Diamond
# Set the line flag
lineAnnotation.Flags = PdfAnnotationFlags.Default
# Set the line color
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Green())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Green())
# Set the leader line
lineAnnotation.LeaderLineExt = 0
lineAnnotation.LeaderLine = 0
# Add the line annotation to the page
page.AnnotationsWidget.Add(lineAnnotation)

# Create second line annotation with different style
linePoints = [100, 550, 280, 550]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the second line annotation")
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Underline
lineAnnotation.lineBorder.BorderWidth = 2
lineAnnotation.LineIntent = PdfLineIntent.LineArrow
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.Circle
lineAnnotation.EndLineStyle = PdfLineEndingStyle.Diamond
lineAnnotation.Flags = PdfAnnotationFlags.Default
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Pink())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Pink())
lineAnnotation.LeaderLineExt = 0
lineAnnotation.LeaderLine = 0
page.AnnotationsWidget.Add(lineAnnotation)

# Create third line annotation with different style
linePoints = [100, 450, 280, 450]
lineAnnotation = PdfLineAnnotation(linePoints, "This is the third line annotation")
lineAnnotation.lineBorder.BorderStyle = PdfBorderStyle.Beveled
lineAnnotation.lineBorder.BorderWidth = 2
lineAnnotation.LineIntent = PdfLineIntent.LineDimension
lineAnnotation.BeginLineStyle = PdfLineEndingStyle.none
lineAnnotation.EndLineStyle = PdfLineEndingStyle.none
lineAnnotation.Flags = PdfAnnotationFlags.Default
lineAnnotation.InnerLineColor = PdfRGBColor(Color.get_Blue())
lineAnnotation.BackColor = PdfRGBColor(Color.get_Blue())
lineAnnotation.LeaderLineExt = 1
lineAnnotation.LeaderLine = 1
page.AnnotationsWidget.Add(lineAnnotation)
```

---

# spire.pdf python link annotation
## create PDF link annotation
```python
#Create a new object of PdfDocument.
doc = PdfDocument()
#Add a page to it.
page = doc.Pages.Add()
#Declare two parameters that will be passed to the constructor of PdfFileLinkAnnotation class.
rect = RectangleF(0.0, 40.0, 250.0, 35.0)
#Create a file link annotation based on the two parameters and add the annotation to the new page.
link = PdfFileLinkAnnotation(rect, "./Demos/Data/Template_Pdf_3.pdf")
page.AnnotationsWidget.Add(link)
#Create a free text annotation based on the same RectangleF, specifying the content.
text = PdfFreeTextAnnotation(rect)
text.Text = "Click here! This is a link annotation."
font = PdfFont(PdfFontFamily.Helvetica, 15.0)
text.Font = font
page.AnnotationsWidget.Add(text)
```

---

# PDF Polygon Annotation Creation
## Create and configure a polygon annotation in PDF document
```python
#Initialize an instance of PdfPolygonAnnotation, specifying all vertex coordinates which can form a complete shape.
polygon = PdfPolygonAnnotation(page, [PointF(0.0, 30.0), PointF(30.0, 15.0), PointF(60.0, 30.0), PointF(45.0, 50.0), PointF(15.0, 50.0), PointF(0.0, 30.0)])
#Set the border color, text, border effect and other properties of polygon annotation.
polygon.Color = PdfRGBColor(Color.get_PaleVioletRed())
polygon.Text = "This is a polygon annotation"
polygon.Author = "E-ICEBLUE"
polygon.Subject = "polygon annotation demo"
polygon.BorderEffect = PdfBorderEffect.BigCloud
polygon.ModifiedDate = DateTime.get_Now()
#Add the annotation to Pdf page
page.AnnotationsWidget.Add(polygon)
```

---

# Spire.PDF Polyline Annotation
## Create a polyline annotation in PDF document
```python
#Create a pdf document
pdf = PdfDocument()
#Add a new page
page = pdf.Pages.Add()
#Create a polyline annotation
polyline = PdfPolyLineAnnotation(page, [PointF(0.0, 60.0), PointF(30.0, 45.0), PointF(60.0, 90.0), PointF(90.0, 80.0)])
#Set properties of polyline
polyline.Color = PdfRGBColor(Color.get_PaleVioletRed())
polyline.Text = "This is a polygon annotation"
polyline.Author = "E-ICEBLUE"
polyline.Subject = "polygon annotation demo"
polyline.Name = "Test Annotation"
polyline.Border = PdfAnnotationBorder(1)
polyline.ModifiedDate = DateTime.get_Now()
#Add the annotation into page
page.AnnotationsWidget.Add(polyline)
```

---

# Spire.PDF Python Annotation Management
## Delete all annotations from a PDF document
```python
#Remove all annotations
document.Pages[0].AnnotationsWidget.Clear()
```

---

# Spire.PDF Annotation Management
## Delete annotation from PDF document
```python
# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Remove the first annotation
doc.Pages[0].AnnotationsWidget.RemoveAt(0)
# Save pdf document
doc.SaveToFile(outputFile)
doc.Close()
```

---

# Extract 3D Video from PDF Annotations
## This code demonstrates how to extract 3D video files from PDF annotations and save them as .u3d files
```python
#Get the first page
firstPage = pdf.Pages[0]
#Get the annotation collection of the first page
annot = firstPage.AnnotationsWidget
#Define an int variable
count = 0
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, Pdf3DAnnotation):
            annot3D = annot[i] if isinstance(annot[i], Pdf3DAnnotation) else None
            #Get the 3D video data
            strData = annot3D._3DData
            if strData is not None:
                #Write the data into .u3d format file
                strData.Save("""3d-{0:d}.u3d""".format(count))
                count += 1
```

---

# Spire.PDF for Python - Get Annotations
## Extract all annotations from a PDF page
```python
#Get all annotations from the first page
annotations = pdf.Pages[0].AnnotationsWidget
sb = []
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #Skip PdfPopupAnnotationWidget
        if isinstance(annotation, PdfPopupAnnotationWidget):
            continue
        sb.append("Annotation information: ")
        sb.append("Text: " + annotation.Text)
        modifiedDate = annotation.ModifiedDate.ToString()
        sb.append("ModifiedDate: " + modifiedDate)
```

---

# spire.pdf python annotation
## get text annotation information from pdf
```python
#Create a new PDF document.
pdf = PdfDocument()
#Load the file from disk.
pdf.LoadFromFile(inputFile)
#Get the annotation collection from the document.
annotations = pdf.Pages[0].AnnotationsWidget
sb = []
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #Get particular annotation information from the document.
        if isinstance(annotation, PdfTextAnnotationWidget):
            sb.append("Annotation information: ")
            sb.append("Text: " + annotation.Text)
            modifiedDate = annotation.ModifiedDate.ToString()
            sb.append("ModifiedDate: " + modifiedDate)
            sb.append("Annotation text: " + annotation.Text)
            sb.append("Annotation ModifiedDate: " + annotation.ModifiedDate.ToString())
            sb.append("Annotation author: " + annotation.Author)
            sb.append("Annotation Name: " + annotation.Name)
pdf.Close()
```

---

# Spire.PDF Invisible Free Text Annotation
## Create invisible and visible free text annotations in PDF
```python
# Get the first page of PDF file
page = doc.Pages[0]

# Add a free text annotation to the page and set it invisible
rect = RectangleF(100.0, 120.0, 150.0, 30.0)
FreetextAnnotation = PdfFreeTextAnnotation(rect)
FreetextAnnotation.Text = "Invisible Free Text Annotation"
font = PdfFont(PdfFontFamily.TimesRoman, 10.0)
border = PdfAnnotationBorder(1.0)
FreetextAnnotation.Font = font
FreetextAnnotation.Border = border
FreetextAnnotation.BorderColor = PdfRGBColor(Color.get_Purple())
FreetextAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
FreetextAnnotation.Color = PdfRGBColor(Color.get_Green())
FreetextAnnotation.Opacity = 0.8
# Set invisible free text annotation
FreetextAnnotation.pipeFlags(PdfAnnotationFlags.Print.value | PdfAnnotationFlags.NoView.value)
page.AnnotationsWidget.Add(FreetextAnnotation)

# Add a free text annotation show it on the page
rect = RectangleF(100.0, 180.0, 150.0, 30.0)
FreetextAnnotation = PdfFreeTextAnnotation(rect)
FreetextAnnotation.Text = "Show Free Text Annotation"
FreetextAnnotation.Font = font
FreetextAnnotation.Border = border
FreetextAnnotation.BorderColor = PdfRGBColor(Color.get_LightPink())
FreetextAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
FreetextAnnotation.Color = PdfRGBColor(Color.get_LightGreen())
FreetextAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(FreetextAnnotation)
```

---

# spire.pdf python annotation
## set free text annotation style in pdf
```python
#Get the first page of PDF file.
page = doc.Pages[0]
#Initialize a PdfFreeTextAnnotation.
rect = RectangleF(150.0, 120.0, 150.0, 30.0)
textAnnotation = PdfFreeTextAnnotation(rect)
#Specify content.
textAnnotation.Text = "\nFree Text Annotation Formatting"
#Set free text annotation formatting and add it to page.
font = PdfFont(PdfFontFamily.TimesRoman, 10.0)
border = PdfAnnotationBorder(1.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Purple())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
textAnnotation.Color = PdfRGBColor(Color.get_Green())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 200.0, 150.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nFree Text Annotation Formatting"
border = PdfAnnotationBorder(1.0)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_LightGoldenrodYellow())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightPink())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 280.0, 280.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\noHow to Set Free Text Annotation Formatting in Pdf file"
border = PdfAnnotationBorder(1)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Gray())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
textAnnotation.Color = PdfRGBColor(Color.get_LightSkyBlue())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
rect = RectangleF(150.0, 360.0, 200.0, 40.0)
textAnnotation = PdfFreeTextAnnotation(rect)
textAnnotation.Text = "\nFree Text Annotation Formatting"
border = PdfAnnotationBorder(1.0)
font = PdfFont(PdfFontFamily.Helvetica, 10.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Pink())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.RClosedArrow
textAnnotation.Color = PdfRGBColor(Color.get_LightGreen())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
```

---

# Spire.PDF Free Text Annotation
## Set subject and properties for a free text annotation in PDF
```python
#Get the first page of PDF file.
page = doc.Pages[0]
#Initialize a PdfFreeTextAnnotation.
rect = RectangleF(150.0, 120.0, 150.0, 30.0)
textAnnotation = PdfFreeTextAnnotation(rect)
#Specify content.
textAnnotation.Text = "\nSet free text annotation subject"
#Set subject.
textAnnotation.Subject = "SubjectTest"
#Set free text annotation formatting and add it to page.
font = PdfFont(PdfFontFamily.TimesRoman, 10.0)
border = PdfAnnotationBorder(1.0)
textAnnotation.Font = font
textAnnotation.Border = border
textAnnotation.BorderColor = PdfRGBColor(Color.get_Purple())
textAnnotation.LineEndingStyle = PdfLineEndingStyle.Circle
textAnnotation.Color = PdfRGBColor(Color.get_Green())
textAnnotation.Opacity = 0.8
page.AnnotationsWidget.Add(textAnnotation)
```

---

# Spire.PDF Text Annotation Properties
## Copy text annotation properties from one PDF to another
```python
# Get the first page
firstPage = pdf.Pages[0]
# Create a new PDF document
newPdf = PdfDocument()
# Traverse the annotations of the first page of old PDF
annot = firstPage.AnnotationsWidget
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        # Get the TextWebLink Annotation
        if isinstance(annotation, PdfFreeTextAnnotationWidget):
            # Get its bounds and text
            rect = annotation.Bounds
            text = annotation.Text
            # Add new page for newPdf
            newPage = newPdf.Pages.Add(firstPage.Size)
            # Add annotation with the same settings as the annotation of old PDF
            newAnnotation = PdfFreeTextAnnotation(rect)
            newAnnotation.Text = text
            newAnnotation.CalloutLines = annotation.CalloutLines
            newAnnotation.LineEndingStyle = annotation.LineEndingStyle
            newAnnotation.AnnotationIntent = PdfAnnotationIntent.FreeTextCallout
            newAnnotation.RectangleDifferences = annotation.RectangularDifferenceArray
            newAnnotation.Color = annotation.Color
            newPage.AnnotationsWidget.Add(newAnnotation)
```

---

# Spire.PDF Update Free Text Annotation
## Update the color of free text annotations in a PDF document
```python
#Get the annotation Collection from the document.
annotations = pdf.Pages[0].AnnotationsWidget
#Update free text annotation.
if annotations.Count > 0:
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        annotation.Color = PdfRGBColor(Color.get_YellowGreen())
```

---

# Spire.PDF Attachments
## Add attachments and attachment annotations to PDF documents
```python
#Add an attachment
attachment = PdfAttachment("Header.png")
streamData = Stream("./Demos/Data/Header.png" )
attachment.Data = streamData.ToArray()
attachment.Description = "Page header picture of demo."
attachment.MimeType = "image/png"
doc.Attachments.Add(attachment)

#Add an attachment
attachment = PdfAttachment("Footer.png")
streamData = Stream("./Demos/Data/Footer.png" )
attachment.Data = streamData.ToArray()
attachment.Description = "Page footer picture of demo."
attachment.MimeType = "image/png"
doc.Attachments.Add(attachment)

#Create attachment annotations
#First annotation
data = Stream("./Demos/Data/SalesReportChart.png" )
annotation1 = PdfAttachmentAnnotation(bounds, "SalesReportChart.png", data)
annotation1.Color = PdfRGBColor(Color.get_Teal())
annotation1.Flags = PdfAnnotationFlags.ReadOnly
annotation1.Icon = PdfAttachmentIcon.Graph
annotation1.Text = "Sales Report Chart"
page.AnnotationsWidget.Add(annotation1)

#Second annotation
data = Stream("./Demos/Data/SciencePersonificationBoston.jpg" )
annotation2 = PdfAttachmentAnnotation(bounds, "SciencePersonificationBoston.jpg", data)
annotation2.Color = PdfRGBColor(Color.get_Orange())
annotation2.Flags = PdfAnnotationFlags.NoZoom
annotation2.Icon = PdfAttachmentIcon.PushPin
annotation2.Text = "SciencePersonificationBoston.jpg, from Wikipedia, the free encyclopedia"
page.AnnotationsWidget.Add(annotation2)

#Third annotation
data = Stream("./Demos/Data/Wikipedia_Science.png" )
annotation3 = PdfAttachmentAnnotation(bounds, "Wikipedia_Science.png", data)
annotation3.Color = PdfRGBColor(Color.get_SaddleBrown())
annotation3.Flags = PdfAnnotationFlags.Locked
annotation3.Icon = PdfAttachmentIcon.Tag
annotation3.Text = "Wikipedia_Science.png, from Wikipedia, the free encyclopedia"
page.AnnotationsWidget.Add(annotation3)

#Fourth annotation
data = Stream("./Demos/Data/PT_Serif-Caption-Web-Regular.ttf" )
annotation4 = PdfAttachmentAnnotation(bounds, "PT_Serif-Caption-Web-Regular.ttf", data)
annotation4.Color = PdfRGBColor(Color.get_CadetBlue())
annotation4.Flags = PdfAnnotationFlags.NoRotate
annotation4.Icon = PdfAttachmentIcon.Paperclip
annotation4.Text = "PT_Serif-Caption-Web-Regular, from https://company.paratype.com"
page.AnnotationsWidget.Add(annotation4)
```

---

# PDF Attachment Management
## Delete all attachments from a PDF document
```python
#Get all attachments
attachments = doc.Attachments
#Delete all attachments
attachments.Clear()
```

---

# Spire.PDF for Python - Get Attachments
## Extract all attachments from a PDF document
```python
# Create a new PDF document
pdf = PdfDocument()
# Load the file from disk
pdf.LoadFromFile("input.pdf")
# Get a collection of attachments on the PDF document
collection = pdf.Attachments
# Save all the attachments to files
if collection.Count > 0:
    for i in range(collection.Count):
        attitem = collection.get_Item(i)
        attitem.Data.Save(attitem.FileName)
pdf.Close()
```

---

# Spire.PDF Get Individual Attachment
## Extract a specific attachment from a PDF document
```python
# Create a new PDF document
pdf = PdfDocument()
# Get a collection of attachments on the PDF document
collection = pdf.Attachments
# Get the second attachment in PDF file
attachment = collection.get_Item(1)
```

---

# Spire.PDF get attachment information
## Extract PDF attachment details including filename, description, and dates
```python
#Create a new PDF document
pdf = PdfDocument()
#Get a collection of attachments on the PDF document
collection = pdf.Attachments
#Get the first attachment
attachment = collection.get_Item(0)
#Get the information of the first attachment
content = []
content.append("Filename: " + attachment.FileName)
content.append("Description: " + attachment.Description)
content.append("Creation Date: " + attachment.CreationDate.ToString())
content.append("Modification Date: " + attachment.ModificationDate.ToString())
pdf.Close()
```

---

# PDF Attachment Relationship
## Create and add attachment with relationship to PDF document
```python
#Create a pdf document
doc= PdfDocument()
#Define PdfAttachment
attachment = PdfAttachment(input_Img)
#Add addachment
doc.Attachments.Add(attachment, doc, PdfAttachmentRelationship.Alternative)
```

---

# spire.pdf python sort attachments
## sort files in pdf document by custom fields
```python
#Create a pdf document
doc = PdfDocument()
doc.Collection.AddCustomField("No", "number", CustomFieldType.NumberField)
doc.Collection.AddFileRelatedField("Desc", "desc", FileRelatedFieldType.Desc)
doc.Collection.Sort(["No", "Desc"], [True, True])
pdfAttachment = PdfAttachment(inputFile1)
doc.Collection.AddAttachment(pdfAttachment)
pdfAttachment = PdfAttachment(inputFile2)
doc.Collection.AddAttachment(pdfAttachment)
pdfAttachment = PdfAttachment(inputFile3)
doc.Collection.AddAttachment(pdfAttachment)
i = 1
for attachment in doc.Collection.AssociatedFiles:
    attachment.SetFieldValue("No", i)
    attachment.SetFieldValue("Desc", attachment.FileName)
    i += 1
```

---

# PDF Bookmark Creation
## Create parent and child bookmarks in a PDF document
```python
# Create PDF document
doc = PdfDocument()

# Set up page margins and size
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
section = doc.Sections.Add()
section.PageSettings.Margins = margin
section.PageSettings.Size = PdfPageSize.A4()

# Create pages and add content
page = section.Pages.Add()
y = 10.0
brush1 = PdfBrushes.get_Black()
font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
format1 = PdfStringFormat(PdfTextAlignment.Center)
page.Canvas.DrawString("Spire Pdf For Python BookMark Demo", font1, brush1, page.Canvas.ClientSize.Width / float(2), y, format1)

# Define bookmark structure
vendors = [["First Parent BookMark", "Spire","Demo BookMark","Spire Pdf","Spire Pdf For Python"],
           ["Second Parent BookMark"],
           ["Third Parent BookMark", "First Child BookMark","Second Child BookMark","Third Child BookMark","Fourth Child BookMark"]]

# Create bookmarks
for i in range(len(vendors)):
    if i > 0:
        page = section.Pages.Add()
        y = 0.0
    
    # Create parent bookmark
    vendorTitle = "{0:d}. {1:s}".format(i + 1, vendors[i][0])
    font1 = PdfTrueTypeFont("Arial", 11.0, PdfFontStyle.Bold, True)
    page.Canvas.DrawString(vendorTitle, font1, PdfBrushes.get_Blue(), 0.0, y)
    
    # Add parent bookmark
    vendorBookmarkDest = PdfDestination(page, PointF(0.0, y))
    vendorBookmark = doc.Bookmarks.Add(vendorTitle)
    vendorBookmark.Color = PdfRGBColor(Color.get_SaddleBrown())
    vendorBookmark.DisplayStyle = PdfTextStyle.Bold
    vendorBookmark.Action = PdfGoToAction(vendorBookmarkDest)
    vendorBookmarkColletion = PdfBookmarkCollection(vendorBookmark)
    
    y = y + font1.MeasureString(vendorTitle).Height + 1
    
    # Create child bookmarks
    for j in range(1, len(vendors[i])):
        if j > 1:
            page = section.Pages.Add()
            y = 0.0
            
        # Create child bookmark
        partTitle = "{0:d}.{1:d}. {2:s}".format(i + 1, j, vendors[i][j])
        font1 = PdfTrueTypeFont("Arial", 11.0, PdfFontStyle.Bold, True)
        page.Canvas.DrawString(partTitle, font1, PdfBrushes.get_Brown(), 0.0, y)
        
        # Add child bookmark
        partBookmarkDest = PdfDestination(page, PointF(0.0, y))        
        partBookmark = vendorBookmarkColletion.Add(partTitle)
        partBookmark.Color = PdfRGBColor(Color.get_Coral())
        partBookmark.DisplayStyle = PdfTextStyle.Italic
        partBookmark.Action = PdfGoToAction(partBookmarkDest)
```

---

# Spire.PDF Bookmark Management
## Delete all bookmarks from a PDF document
```python
#Remove all bookmarks from the PDF document
document.Bookmarks.Clear()
```

---

# Spire.PDF Bookmark Deletion
## Delete a bookmark from a PDF document
```python
#Delete the first bookmark
doc.Bookmarks.RemoveAt(0)
```

---

# spire.pdf python expand bookmarks
## Expand bookmarks in a PDF document
```python
#Create a new PDF document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Set BookMarkExpandOrCollapse as true to expand the bookmarks.
doc.ViewerPreferences.BookMarkExpandOrCollapse = True
```

---

# Spire.PDF Bookmark Expansion
## Expand or collapse specific bookmarks in a PDF document
```python
#Set BookMarkExpandOrCollapse as "true" for the first bookmarks 
pdf.Bookmarks.get_Item(0).ExpandBookmark = True
#Set BookMarkExpandOrCollapse as "false" for the second bookmarks 
pdf.Bookmarks.get_Item(1).ExpandBookmark = False
```

---

# Get PDF Bookmark Page Number
## Extract the page number of a bookmark in a PDF document
```python
#Create a new PDF document.
doc = PdfDocument()
#Load a PDF file.
doc.LoadFromFile("input.pdf")
#Get bookmarks collections of the PDF file.
bookmarks = doc.Bookmarks
#Get the page number of the first bookmark.
bookmark = bookmarks[0]
pageNumber = doc.Pages.IndexOf(bookmark.Destination.Page)+1
```

---

# Spire.PDF Python Bookmark Extraction
## Extract bookmarks from a PDF document
```python
def GetChildBookmark(parentBookmark, content):
    if parentBookmark.Count > 0:
        for i in range(parentBookmark.Count):
            childBookmark = parentBookmark.get_Item(i)
            # Get the title.
            content.append(childBookmark.Title)
            # Get the text style.
            textStyle = str(childBookmark.DisplayStyle)
            content.append(textStyle)
            cldBk = PdfBookmarkCollection(childBookmark)
            GetChildBookmark(cldBk, content)
        
def GetBookmarks(bookmarks, result):
    # Declare a new content list
    content = []
    # Get Pdf bookmarks information.
    if bookmarks.Count > 0:
        content.append("Pdf bookmarks:")
        for i in range(bookmarks.Count):
            parentBookmark = bookmarks.get_Item(i)
            # Get the title.
            content.append(parentBookmark.Title)
            # Get the text style.
            textStyle = str(parentBookmark.DisplayStyle)
            content.append(textStyle)
            cldBk = PdfBookmarkCollection(parentBookmark)
            GetChildBookmark(cldBk, content)

# Create a new Pdf document.
doc = PdfDocument()
# Load the file from disk.
doc.LoadFromFile(inputFile)
# Get bookmarks collection of the Pdf file.
bookmarks = doc.Bookmarks
# Get Pdf Bookmarks.
GetBookmarks(bookmarks, outputFile)
doc.Close()
```

---

# Spire.PDF Python Get Child Bookmarks
## Extract child bookmark information from a PDF document including title, color, and text style

```python
def GetChildBookmarks(bookmarks):
    #Get Pdf child Bookmarks information.
    for i in range(bookmarks.Count):
        parentBookmark = bookmarks.get_Item(i)
        cldBk = PdfBookmarkCollection(parentBookmark)
        if cldBk.Count > 0:
            for j in range(cldBk.Count):
                childBookmark = cldBk.get_Item(j)
                #Get the title
                title = childBookmark.Title
                #Get the color.
                color = str(childBookmark.Color)
                colorR = color.split(' ')[0][1:len(color.split(' ')[0])]
                #Get the text style.
                textStyle = str(childBookmark.DisplayStyle)

#Create a new Pdf document.
doc = PdfDocument()
#Load the file from disk.
doc.LoadFromFile(inputFile)
#Get bookmarks collections of the PDF file.
bookmarks = doc.Bookmarks
#Get Pdf child Bookmarks.
GetChildBookmarks(bookmarks)
doc.Close()
```

---

# Spire.PDF Bookmark Zoom Setting
## Set zoom level for PDF bookmarks
```python
#Get bookmarks collections of the PDF file
bookmarks = pdfdoc.Bookmarks
#Set Zoom level as 0, which the value is inherit zoom
for i in range(bookmarks.Count):
    bookMark = bookmarks.get_Item(i)
    bookMark.Destination.Zoom = 0.5
```

---

# spire.pdf python bookmark
## update bookmarks in pdf document
```python
def EditChildBookmark(parentBookmark):
    pBookmark = PdfBookmarkCollection(parentBookmark)
    for i in range(pBookmark.Count):
        childBookmark = pBookmark.get_Item(i)
        childBookmark.Color = PdfRGBColor(Color.get_Blue())
        childBookmark.DisplayStyle = PdfTextStyle.Regular
        EditChild2Bookmark(childBookmark)

def EditChild2Bookmark(childBookmark):
    cldBookmark = PdfBookmarkCollection(childBookmark)
    for i in range(cldBookmark.Count):
        child2Bookmark = cldBookmark.get_Item(i)
        child2Bookmark.Color = PdfRGBColor(Color.get_LightSalmon())
        child2Bookmark.DisplayStyle = PdfTextStyle.Italic

#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Get the first bookmark
bookmark = doc.Bookmarks[0]
#Change the title of the bookmark
bookmark.Title = "Modified BookMark"
#Set the color of the bookmark
bookmark.Color = PdfRGBColor(Color.get_Black())
#Set the outline text style of the bookmark
bookmark.DisplayStyle = PdfTextStyle.Bold
#Edit child bookmarks of the parent bookmark
EditChildBookmark(bookmark)
#Save the pdf document
doc.SaveToFile(outputFile)
doc.Close()
```

---

# Spire.PDF Python ListBox Field
## Add a list box field to a PDF document
```python
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
```

---

# Spire.PDF TextBox Field
## Add a TextBox field to a PDF document
```python
#Enable form creation for the PDF
pdf.AllowCreateForm = True
#Get the first page
page = pdf.Pages[0]
#Create a new pdf font
font = PdfFont(PdfFontFamily.Helvetica, 12.0, PdfFontStyle.Bold)
#Create a pdf brush
brush = PdfBrushes.get_Black()
x = 50.0
y = 550.0
tempX = 0
text = "TexBox: "
#Draw a text into page
page.Canvas.DrawString(text, font, brush, x, y)
#Add a textBox field
tempX = font.MeasureString(text).Width + x + 15
textbox = PdfTextBoxField(page, "TextBox")
textbox.Bounds = RectangleF(tempX, y, 100.0, 15.0)
textbox.BorderWidth = 0.75
textbox.BorderStyle = PdfBorderStyle.Solid
pdf.Form.Fields.Add(textbox)
```

---

# Spire.PDF Form Field Tooltip
## Add tooltip to form field in PDF document
```python
# Get the first page
page = doc.Pages[0]
# As for existing pdf, the property needs to be set as true
doc.AllowCreateForm = True
# Create a pdf textbox field
textbox = PdfTextBoxField(page, "TextBox")
# Set the bounds of textbox field
textbox.Bounds = RectangleF(100.0, 100.0, 100.0, 15.0)
# Set the border width of textbox field
textbox.BorderWidth = 0.75
# Set the border style of textbox field
textbox.BorderStyle = PdfBorderStyle.Solid
# Add the textbox field into pdf document
doc.Form.Fields.Add(textbox)
# Add a tooltip for the textbox field
doc.Form.Fields.get_Item("TextBox").ToolTip = "Please insert a valid email address"
```

---

# Spire.PDF Button Field with Icons
## Assign icons to button field in different states and configure icon layout
```python
# Create a Button
btn = PdfButtonField(page, "button1")
btn.Bounds = RectangleF(0.0, 50.0, 120.0, 100.0)
btn.HighlightMode = PdfHighlightMode.Push
btn.LayoutMode = PdfButtonLayoutMode.CaptionOverlayIcon
# Set text and icon for Normal appearance
btn.Text = "Normal Text"
btn.Icon = PdfImage.FromFile("image_path")
# Set text and icon for Click appearance (Can only be set when highlight mode is Push)
btn.AlternateText = "Alternate Text"
btn.AlternateIcon = PdfImage.FromFile("image_path")
# Set text and icon for Rollover appearance (Can only be set when highlight mode is Push)
btn.RolloverText = "Rollover Text"
btn.RolloverIcon = PdfImage.FromFile("image_path")
# Set icon layout
btn.IconLayout.Spaces = [0.5, 0.5]
btn.IconLayout.ScaleMode = PdfButtonIconScaleMode.Proportional
btn.IconLayout.ScaleReason = PdfButtonIconScaleReason.Always
btn.IconLayout.IsFitBounds = False
# Add the button to the document
doc.Form.Fields.Add(btn)
```

---

# Spire.PDF Automatic Fields
## Creating and drawing various automatic fields in a PDF document
```python
def DrawAutomaticFieldP(page):
    y = 20.0

    #Title
    brush1 = PdfBrushes.get_CadetBlue()
    font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
    format1 = PdfStringFormat(PdfTextAlignment.Center)
    page.Canvas.DrawString("Automatic Field List", font1, brush1, page.Canvas.ClientSize.Width / float(2), y, format1)
    y = y + font1.MeasureString("Automatic Field List", format1).Height
    y = y + 15
    fieldList = ["DateTimeField", "CreationDateField", "DocumentAuthorField", "SectionNumberField", "SectionPageNumberField", "SectionPageCountField", "PageNumberField", "PageCountField", "DestinationPageNumberField", "CompositeField"]
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular ,True)
    fieldNameFormat = PdfStringFormat()
    fieldNameFormat.MeasureTrailingSpaces = True
    for fieldName in fieldList:
        #Draw field name
        text = "{0:s}: ".format(fieldName)
        page.Canvas.DrawString(text, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
        x = font.MeasureString(text, fieldNameFormat).Width
        bounds = RectangleF(x, y, 200.0, font.Height)
        DrawAutomaticField(fieldName, page, bounds)
        y = y + font.Height + 8

def DrawAutomaticField(fieldName, page, bounds):
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Italic,True)
    brush = PdfBrushes.get_OrangeRed()
    format = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)
    if "DateTimeField" == fieldName:
        field = PdfDateTimeField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.DateFormatString = "yyyy-MM-dd HH:mm:ss"
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "CreationDateField" == fieldName:
        field = PdfCreationDateField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.DateFormatString = "yyyy-MM-dd HH:mm:ss"
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "DocumentAuthorField" == fieldName:
        field = PdfDocumentAuthorField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionNumberField" == fieldName:
        field = PdfSectionNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionPageNumberField" == fieldName:
        field = PdfSectionPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "SectionPageCountField" == fieldName:
        field = PdfSectionPageCountField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "PageNumberField" == fieldName:
        field = PdfPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "PageCountField" == fieldName:
        field = PdfPageCountField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "DestinationPageNumberField" == fieldName:
        field = PdfDestinationPageNumberField()
        field.Font = font
        field.Brush = brush
        field.StringFormat = format
        field.Bounds = bounds
        field.Page = page if isinstance(page, PdfNewPage) else None
        graWidget = PdfGraphicsWidget(field)
        graWidget.Draw(page.Canvas)
    if "CompositeField" == fieldName:
        field1 = PdfSectionPageNumberField()
        field1.NumberStyle = PdfNumberStyle.LowerRoman
        field2 = PdfSectionPageCountField()
        fields = PdfCompositeField()
        fields.Font = font
        fields.Brush = brush
        fields.StringFormat = format
        fields.Bounds = bounds
        fields.AutomaticFields = [field1, field2]
        fields.Text = "section page {0} of {1}"
        graWidget = PdfGraphicsWidget(fields)
        graWidget.Draw(page.Canvas)
```

---

# Spire.PDF Form Field Location Modification
## Change the location of a specific form field in a PDF document
```python
# Access PDF form
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None            
            # Find the textbox named TextBox1
            if textbox.Name == "TextBox1":
                # Change field location
                textbox.Location = PointF(390.0, 525.0)
```

---

# Spire.PDF Form Field Deletion
## Delete a specific form field from a PDF document
```python
# Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
# Find the particular form field and delete it
if formWidget.FieldsWidget.Count > 0:
    i = 0
    while i < formWidget.FieldsWidget.Count:
        field = formWidget.FieldsWidget.get_Item(i)

        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            if textbox.Name == "password2":
                formWidget.FieldsWidget.Remove(textbox)
        i = i + 1
```

---

# Spire.PDF form field requirement
## Determine and set required fields in PDF forms
```python
# Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
# Find the particular form field and determine if it marks as required or not
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)

        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            if textbox.Name == "username":
                textbox.Required = True
            if textbox.Name == "password2":
                textbox.Required = False
```

---

# PDF JavaScript Extraction
## Extract JavaScript from PDF form fields
```python
#Create a pdf document
pdf = PdfDocument()
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Find the FieldsWidget
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
        #Find the textbox named total
        if textbox.Name == "total":
            #Get the action
            jsa = textbox.Actions.Calculate
            if jsa is not None:
                #Get JavaScript
                js = jsa.Script
```

---

# Spire.PDF Form Field Filling
## Fill various types of form fields in a PDF document
```python
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Find the FieldsWidget
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textBoxField = field if isinstance(field, PdfTextBoxFieldWidget) else None
            if textBoxField.Name == "email":
                textBoxField.Text = "support@e-iceblue.com"
            elif textBoxField.Name == "username":
                textBoxField.Text = "E-iceblue"
            elif textBoxField.Name == "password":
                textBoxField.Password = True
                textBoxField.Text = "e-iceblue"
            elif textBoxField.Name == "password2":
                textBoxField.Password = True
                textBoxField.Text = "e-iceblue"
            elif textBoxField.Name == "company_name ":
                textBoxField.Text = "E-iceblue"
            elif textBoxField.Name == "first_name":
                textBoxField.Text = "James"
            elif textBoxField.Name == "last_name":
                textBoxField.Text = "Chen"
            elif textBoxField.Name == "middle_name":
                textBoxField.Text = "J"
            elif textBoxField.Name == "address1":
                textBoxField.Text = "Chengdu"
            elif textBoxField.Name == "address2":
                textBoxField.Text = "Beijing"
            elif textBoxField.Name == "city":
                textBoxField.Text = "Shanghai"
            elif textBoxField.Name == "postal_code":
                textBoxField.Text = "11111"
            elif textBoxField.Name == "state":
                textBoxField.Text = "Shanghai"
            elif textBoxField.Name == "phone":
                textBoxField.Text = "1234567901"
            elif textBoxField.Name == "mobile_phone":
                textBoxField.Text = "123456789"
            elif textBoxField.Name == "fax":
                textBoxField.Text = "12121212"
        if isinstance(field, PdfListBoxWidgetFieldWidget):
            listBoxField = field if isinstance(field, PdfListBoxWidgetFieldWidget) else None
            if listBoxField.Name == "email_format":
                index = [1]
                listBoxField.SelectedIndex = index
        if isinstance(field, PdfComboBoxWidgetFieldWidget):
            comBoxField = field if isinstance(field, PdfComboBoxWidgetFieldWidget) else None
            if comBoxField.Name == "title":
                items = [0]
                comBoxField.SelectedIndex = items
        if isinstance(field, PdfRadioButtonListFieldWidget):
            radioBtnField = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
            if radioBtnField.Name == "country":
                radioBtnField.SelectedIndex = 1
        if isinstance(field, PdfCheckBoxWidgetFieldWidget):
            checkBoxField = field if isinstance(field, PdfCheckBoxWidgetFieldWidget) else None
            if checkBoxField.Name == "agreement_of_terms":
                checkBoxField.Checked = True
        if isinstance(field, PdfButtonWidgetFieldWidget):
            btnField = field if isinstance(field, PdfButtonWidgetFieldWidget) else None
            if btnField.Name == "submit":
                btnField.Text = "Submit"
```

---

# PDF Form Button Field Image Filling
## Fill an image into a button field in a PDF form
```python
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
#Traverse all the forms
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfButtonWidgetFieldWidget):
            field = field if isinstance(field, PdfButtonWidgetFieldWidget) else None
            if field.Name == "Button1":
                #Set "true" to fit bounds
                field.IconLayout.IsFitBounds = True
                #Fill the annotation rectangle exactly without its original aspect ratio
                field.IconLayout.ScaleMode = PdfButtonIconScaleMode.Anamorphic
                #Fill an image
                field.SetButtonImage(PdfImage.FromFile(inputImage))
```

---

# PDF Form Field Flattening
## This code demonstrates how to flatten form fields in a PDF document
```python
# Flatten form fields
doc.Form.IsFlatten = True
```

---

# Spire.PDF get form field coordinates
## Extract coordinates of a textbox field from a PDF form
```python
#Create a pdf document
doc = PdfDocument()
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Get textbox
field = formWidget.FieldsWidget.get_Item("Text1")
textbox = PdfTextBoxFieldWidget(field.Ptr)
#Get the location of the textbox
location = textbox.Location
```

---

# Spire.PDF Get Form Field Value
## Extract text value from a form field in a PDF document
```python
# Create a pdf document
doc = PdfDocument()
# Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
# Get textbox
field = formWidget.FieldsWidget.get_Item("Text1")
textbox = PdfTextBoxFieldWidget(field.Ptr)
# Get the text of the textbox
text = textbox.Text
```

---

# Spire.PDF Get Radio Button Style
## Extract the style information of radio button fields in a PDF form
```python
# Open pdf document
pdf = PdfDocument()
# Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
# Traverse all the forms
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        # Find the radio button field
        if isinstance(field, PdfRadioButtonListFieldWidget):
            radio = field
            # Get the button style
            buttonStyle = radio.ButtonStyle
```

---

# spire.pdf form field extraction
## get values from all form fields in a pdf document
```python
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
sb = []
#Traverse all the forms
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textBoxField = field if isinstance(field, PdfTextBoxFieldWidget) else None
            #Get text of textbox
            text = textBoxField.Text
            sb.append("The text in textbox is " + text + "\r\n")
        if isinstance(field, PdfListBoxWidgetFieldWidget):
            listBoxField = field if isinstance(field, PdfListBoxWidgetFieldWidget) else None
            sb.append("Listbox items are \r\n")
            #Get values of listbox
            items = listBoxField.Values
            for i in range(items.Count):
                item = items.get_Item(i)
                sb.append(item.Value + "\r\n")
            #Get selected value
            selectedValue = listBoxField.SelectedValue
            sb.append("The selected value in the listbox is " + selectedValue + "\r\n")
        if isinstance(field, PdfComboBoxWidgetFieldWidget):
            comBoxField = field if isinstance(field, PdfComboBoxWidgetFieldWidget) else None
            sb.append("comBoxField items are \r\n")
            #Get values of comboBox
            items = comBoxField.Values
            for i in range(items.Count):
                item = items.get_Item(i)
                sb.append(item.Value + "\r\n")
            #Get selected value
            selectedValue = comBoxField.SelectedValue
            sb.append("The selected value in the comBoxField is " + selectedValue + "\r\n")
        if isinstance(field, PdfRadioButtonListFieldWidget):
            radioBtnField = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
            #Get value of radio button
            value = radioBtnField.Value
            sb.append("The text in radioButtonField is " + value + "\r\n")
        if isinstance(field, PdfCheckBoxWidgetFieldWidget):
            checkBoxField = field if isinstance(field, PdfCheckBoxWidgetFieldWidget) else None
            #Get the checked state of the checkbox
            state = checkBoxField.Checked
            stateValue = "True" if state else "False"
            sb.append("If the checkBox is checked: " + stateValue + "\r\n")
```

---

# Spire.PDF Form Field Modification
## Modify the value of a text box field in a PDF form
```python
# Access PDF form
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
# Iterate through form fields
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfTextBoxFieldWidget):
            textbox = field if isinstance(field, PdfTextBoxFieldWidget) else None
            # Find the textbox named TextBox1
            if textbox.Name == "TextBox1":
                textbox.Text = "New value"
```

---

# PDF form field recognition
## Identify required fields in a PDF form
```python
# Create a PDF document
doc = PdfDocument()
# Get PDF forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
builder = []
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfField):
            field = field if isinstance(field, PdfField) else None
            # Judge if the field is required
            if field.Required:
                builder.append("The field named: "+ field.Name + " is required")
```

---

# Spire.PDF Form Field Removal
## Remove form fields from PDF documents
```python
# Create a PdfDocument
pdf = PdfDocument()
# Get form from the document
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
if formWidget is not None:
    i = 0
    while i <= formWidget.FieldsWidget.List.Count - 1:
        # Remove the first form field
        if i == 0:
            field = formWidget.FieldsWidget.get_Item(i)
            refield = field if isinstance(field, PdfField) else None
            formWidget.FieldsWidget.Remove(refield)
            break
        i += 1
```

---

# Spire.PDF Radio Button Selection
## Select a specific radio button item in a PDF form
```python
# Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
# Find the field 
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfRadioButtonListFieldWidget):
            radioButton = field if isinstance(field, PdfRadioButtonListFieldWidget) else None
            if radioButton.Name == "RadioButton":
                radioButton.SelectedIndex = 1
```

---

# Spire.PDF Set Export Value for Checkbox
## Set export values for checkbox fields in a PDF form
```python
#Get pdf forms
pdfform = pdf.Form
formWidget = PdfFormWidget(pdfform)
count = 1
#Find the field 
if formWidget.FieldsWidget.Count > 0:
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        if isinstance(field, PdfCheckBoxWidgetFieldWidget):
            checkbox = field if isinstance(field, PdfCheckBoxWidgetFieldWidget) else None
            #Set export value for checkbox
            count+=1
            checkbox.SetExportValue("True" + str(count))
```

---

# Spire.PDF Form Field Font Setting
## Set font for PDF form field
```python
#Get pdf forms
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)
#Get textbox
field = formWidget.FieldsWidget.get_Item("Text1")
textbox = PdfTextBoxFieldWidget(field.Ptr)
#Set the font for textbox
textbox.Font = PdfTrueTypeFont("Tahoma", 12.0, PdfFontStyle.Regular, True)
#Set text
textbox.Text = "Hello World"
```

---

# spire.pdf python stamp
## add date time stamp to pdf
```python
#Get the first page
page = document.Pages[0]
#Set the font and brush
font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Blue()))
#Time text
timeString = DateTime.get_Now().ToString("MM/dd/yy hh:mm:ss tt ")
#Create a template and rectangle, draw the string
template = PdfTemplate(140.0, 15.0)
rect = RectangleF(PointF(page.ActualSize.Width - template.Width - 10, page.ActualSize.Height - template.Height - 10), template.Size)
template.Graphics.DrawString(timeString, font, brush, PointF(0.0, 0.0))
#Create stamp annoation
stamp = PdfRubberStampAnnotation(rect)
apprearance = PdfAppearance(stamp)
apprearance.Normal = template
stamp.Appearance = apprearance
page.AnnotationsWidget.Add(stamp)
```

---

# Spire.PDF Image Stamp
## Add an image stamp to a PDF page
```python
#Get the first page
page = document.Pages[0]
#Create a rubber stamp annotation
loStamp = PdfRubberStampAnnotation(RectangleF(PointF(0.0, 0.0), SizeF(60.0, 60.0)))
#Create an instance of PdfAppearance 
loApprearance = PdfAppearance(loStamp)
image = PdfImage.FromFile("./Demos/Data/image stamp.jpg")
template = PdfTemplate(210.0, 210.0)
#Draw a pdf image into pdf template
template.Graphics.DrawImage(image, 60.0, 60.0)
loApprearance.Normal = template
loStamp.Appearance = loApprearance
#Add the rubber stamp annotation into pdf
page.AnnotationsWidget.Add(loStamp)
```

---

# Spire.PDF Text Stamp
## Add a text stamp to a PDF page
```python
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
path.AddLine(template.GetBounds().X, template.GetBounds().Y + CornerRadius / float(2), template.GetBounds().X, template.GetBounds().Y + CornerRadius / float(2))
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
#Add stamp to page
page.AnnotationsWidget.Add(stamp)
```

---

# Spire.PDF Tiling Background Image
## Add a tiled background image to PDF pages with transparency
```python
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    #Create PdfTilingBrush
    brush = PdfTilingBrush(SizeF(page.Canvas.Size.Width / float(3), page.Canvas.Size.Height / float(5)))
    #Set the transparency
    brush.Graphics.SetTransparency(0.3)
    #Draw image on brush graphics
    brush.Graphics.DrawImage(image, PointF((brush.Size.Width - image.Width) / float(2), (brush.Size.Height - image.Height) / float(2)))
    #use the brush to draw rectangle
    page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.Size))
```

---

# Spire.PDF Python Fill and Stroke Text
## Demonstrates how to add filled and stroked text to a PDF page with rotation and formatting
```python
#Create a pdf document
doc = PdfDocument()
#Get the first page
page = doc.Pages[0]
#Define Pdf pen
pen = PdfPen(PdfRGBColor(Color.get_Gray()))
#Save graphics state
state = page.Canvas.Save()
#Rotate page canvas
page.Canvas.RotateTransform(-20.0)
format = PdfStringFormat()
format.CharacterSpacing = 5.0
#Draw the string on page
page.Canvas.DrawString("E-ICEBLUE", PdfFont(PdfFontFamily.Helvetica, 45.0), pen, 0.0, 500.0,format)
#Restore graphics
page.Canvas.Restore(state)
```

---

# PDF Image Watermark
## Add an image as background watermark to a PDF page
```python
#Get the first page
page = doc.Pages[0]
#Load image
img = Stream(inputFile_img)
#Set background image
page.BackgroundImage = img
```

---

# Spire.PDF Image Watermark
## Add an image as watermark to PDF with transparency

```python
#Get the first page of PDF document
page = doc.Pages[0]
#Set position for watermark
position = PointF(160.0, 260.0)
#Apply watermark with transparency
page.Canvas.Save()
page.Canvas.SetTransparency(0.5, 0.5, PdfBlendMode.Multiply)
page.Canvas.DrawImage(pdfImage, position)
page.Canvas.Restore()
```

---

# PDF Stamp Properties Configuration
## Set properties for rubber stamp annotations in PDF documents
```python
#Get the first page
page = pdf.Pages[0]
#Traverse annotations widget
annot = page.AnnotationsWidget
if annot.Count > 0:
    for i in range(annot.Count):
        annotation = annot.get_Item(i)
        #If it is PdfRubberStampAnnotationWidget
        if isinstance(annotation, PdfRubberStampAnnotationWidget):
            stamp = annotation if isinstance(annotation, PdfRubberStampAnnotationWidget) else None
            stamp.Author = "TestUser"
            stamp.Subject = "E-iceblue"
            stamp.CreationDate = DateTime.get_Now()
            stamp.ModifiedDate = DateTime.get_Now()
```

---

# Spire.PDF Text Watermark
## Create and apply a text watermark to a PDF page
```python
# Get the first page
page = doc.Pages[0]
# Draw text watermark
brush = PdfTilingBrush(SizeF(page.Canvas.ClientSize.Width / float(2), page.Canvas.ClientSize.Height / float(3)))
brush.Graphics.SetTransparency(0.3)
brush.Graphics.Save()
brush.Graphics.TranslateTransform(brush.Size.Width / float(2), brush.Size.Height / float(2))
brush.Graphics.RotateTransform(-45.0)
brush.Graphics.DrawString("Spire.Pdf Demo", PdfFont(PdfFontFamily.Helvetica, 24.0), PdfBrushes.get_Violet(), 0.0, 0.0, PdfStringFormat(PdfTextAlignment.Center))
brush.Graphics.Restore()
brush.Graphics.SetTransparency(1.0)
page.Canvas.DrawRectangle(brush, RectangleF(PointF(0.0, 0.0), page.Canvas.ClientSize))
```

---

# Spire.PDF Python Headers
## Add different headers to PDF pages
```python
# Define header texts
header1 = "Header 1"
header2 = "Header 2"

# Define style for first header
font = PdfTrueTypeFont("Arial", 15.0, PdfFontStyle.Bold, True)
brush = PdfBrushes.get_Red()
rect = RectangleF(PointF(0.0,20.0),SizeF(doc.PageSettings.Size.Width,50.0))
format = PdfStringFormat()
format.Alignment= PdfTextAlignment.Center

# Add first header to page 0
doc.Pages[0].Canvas.DrawString(header1,font,brush,rect,format)

# Define style for second header
font = PdfTrueTypeFont("Aleo", 15.0, PdfFontStyle.Regular,True)
brush = PdfBrushes.get_Black()
format.Alignment = PdfTextAlignment.Left

# Add second header to page 1
doc.Pages[1].Canvas.DrawString(header2, font, brush, rect, format)
```

---

# PDF Header and Footer Implementation
## Add headers and footers to PDF pages
```python
# Create brush, pen, font and alignment for header and footer
brush = PdfBrushes.get_Black()
pen = PdfPen(brush, 0.75)
font = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Italic, True)
rightAlign = PdfStringFormat(PdfTextAlignment.Right)
leftAlign = PdfStringFormat(PdfTextAlignment.Left)
rightAlign.MeasureTrailingSpaces = True
rightAlign.MeasureTrailingSpaces = True
margin = doc.PageSettings.Margins
space = font.Height * 0.75
x = 0.0
y = 0.0
width = 0.0

# Create a new pdf document
newPdf = PdfDocument()
newPage = None

for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Add new page
    newPage = newPdf.Pages.Add(page.Size, PdfMargins(0.0))
    newPage.Canvas.SetTransparency(0.5)
    x = margin.Left
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    y = margin.Top - space
    
    # Draw header line
    newPage.Canvas.DrawLine(pen, x, y + 15, x + width, y + 15)
    y = y + 10 - font.Height
    
    # Draw header image into newPage
    newPage.Canvas.SetTransparency(0.5)
    headerImage = PdfImage.FromFile("./Demos/Data/Header.png")
    newPage.Canvas.DrawImage(headerImage, PointF(0.0, 0.0))
    
    # Draw header text into newPage
    newPage.Canvas.DrawString("Demo of Spire.Pdf", font, brush, x + width, y, rightAlign)
    
    # Draw footer image into newPage
    footerImage = PdfImage.FromFile("./Demos/Data/Footer.png")
    newPage.Canvas.DrawImage(footerImage, PointF(0.0, newPage.Canvas.ClientSize.Height - footerImage.PhysicalDimension.Height))
    
    brush = PdfBrushes.get_DarkBlue()
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Bold, True)
    y = newPage.Canvas.ClientSize.Height - margin.Bottom - font.Height
    
    # Draw footer text into newPage
    newPage.Canvas.DrawString("Created by E-iceblue Co,.Ltd", font, brush, x, y, leftAlign)
    newPage.Canvas.SetTransparency(1.0)
    
    # Draw the page into newPage
    newTemplate = page.CreateTemplate()
    template = PdfGraphicsWidget(newTemplate.Ptr)
    template.Draw(newPage.Canvas, PointF(0.0, 0.0))
```

---

# Spire.PDF Header and Footer with Image and Page Number
## Create PDF headers with images and footers with page numbering
```python
def CreateHeaderTemplate(margins, pageSize):
    # Create a PdfPageTemplateElement object as header space
    headerSpace = PdfPageTemplateElement(pageSize.Width, margins.Top)
    headerSpace.Foreground = False
    # Declare two float variables
    x = margins.Left
    y = 0.0
    # Draw image in header space 
    headerImage = PdfImage.FromFile("./path/to/image.png")  # Using a placeholder path
    width = headerImage.Width / float(2)
    height = headerImage.Height / float(2)
    headerSpace.Graphics.DrawImage(headerImage, x, margins.Top - height - 5, width, height)
    # Draw line in header space
    pen = PdfPen(PdfBrushes.get_LightGray(), 1.0)
    headerSpace.Graphics.DrawLine(pen, x, y + margins.Top - 2, pageSize.Width - x, y + margins.Top - 2)
    # Return headerSpace
    return headerSpace

def CreateFooterTemplate(margins, pageSize):
    # Create a PdfPageTemplateElement object which works as footer space
    footerSpace = PdfPageTemplateElement(pageSize.Width, margins.Bottom)
    footerSpace.Foreground = False
    # Declare two float variables
    x = margins.Left
    y = 0.0
    # Draw line in footer space
    pen = PdfPen(PdfBrushes.get_Gray(), 1.0)
    footerSpace.Graphics.DrawLine(pen, x, y, pageSize.Width - x, y)
    # Draw text in footer space
    y = y + 5
    font = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
    # Draw dynamic field in footer space
    number = PdfPageNumberField()
    count = PdfPageCountField()
    listAutomaticField = [number, count]
    compositeField = PdfCompositeField(font, PdfBrushes.get_Black(), "Page {0} of {1}", listAutomaticField)
    compositeField.StringFormat = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Top)
    size = font.MeasureString(compositeField.Text)
    compositeField.Bounds = RectangleF(x, y, size.Width, size.Height)
    newTemplate = compositeField
    templateGraphicsWidget = PdfGraphicsWidget(newTemplate.Ptr)
    templateGraphicsWidget.Draw(footerSpace.Graphics)
    # Return footerSpace
    return footerSpace

# Create a PDF document
doc = PdfDocument()
doc.PageSettings.Size = PdfPageSize.A4()
# Reset the default margins to 0
doc.PageSettings.Margins = PdfMargins(0.0)
# Create a PdfMargins object, the parameters indicate the page margins you want to set
margins = PdfMargins(50.0, 50.0, 50.0, 50.0)
# Get page size
pageSize = doc.PageSettings.Size
# Create a header template with content and apply it to page template
doc.Template.Top = CreateHeaderTemplate(margins, pageSize)
# Create a footer template with content and apply it to page template
doc.Template.Bottom = CreateFooterTemplate(margins, pageSize)
# Apply blank templates to other parts of page template
docSizeHeight = doc.PageSettings.Size.Height
doc.Template.Left = PdfPageTemplateElement(margins.Left, docSizeHeight)
doc.Template.Right = PdfPageTemplateElement(margins.Right, docSizeHeight)
```

---

# Spire.PDF Header and Footer with Templates
## Add image and text to PDF header and footer using templates
```python
#Get the first page
page = doc.Pages[0]
#Get the margins of Pdf
margin = doc.PageSettings.Margins
#Define font and brush
font = PdfTrueTypeFont("Impact",14.0,PdfFontStyle.Regular,True)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Gray()))
#Load an image
image = PdfImage.FromFile("./Demos/Data/E-iceblueLogo.png")
#Specify the image size
imageSize = SizeF(image.Width / float(2),image.Height / float(2))
#Create a header template
headerTemplate = PdfTemplate(page.ActualSize.Width - margin.Left - margin.Right, imageSize.Height)
#Draw the image in the template
headerTemplate.Graphics.DrawImage(image, PointF(0.0, 0.0),imageSize)
#Create a retangle
rect = headerTemplate.GetBounds()
#string format
format1 = PdfStringFormat(PdfTextAlignment.Right,PdfVerticalAlignment.Middle)
#Draw a string in the template
headerTemplate.Graphics.DrawString("Header", font, brush, rect, format1)
#Create a footer template and draw a text
footerTemplate = PdfTemplate(page.ActualSize.Width - margin.Left - margin.Right, imageSize.Height)
format2 = PdfStringFormat(PdfTextAlignment.Center,PdfVerticalAlignment.Middle)
footerTemplate.Graphics.DrawString("Footer", font, brush, rect, format2)
x = margin.Left
y = 0.0
#Draw the header template on page at specified location
page.Canvas.DrawTemplate(headerTemplate, PointF(x,y))
#Draw the footer template on page at specified location
y = page.ActualSize.Height - footerTemplate.Height - 10
page.Canvas.DrawTemplate(footerTemplate, PointF(x, y))
```

---

# Spire.PDF Python Header and Footer
## Add inline image and text to PDF header/footer
```python
# Define text content
text1 = "Spire.Pdf is a robust component by"
text2 = "Technology Co., Ltd."
image = PdfImage.FromFile("./Demos/Data/Top-logo.png")

# Define font and brush
font = PdfTrueTypeFont("Impact", 10.0, PdfFontStyle.Regular, True)
bursh = PdfBrushes.get_DarkGray()

# Get the size of text
s1 = font.MeasureString(text1)
s2 = font.MeasureString(text2)
x = 10.0
y = 10.0

# Define image size
imgSize = SizeF(image.Width / float(2), image.Height / float(2))

# Define rectangle and string format
size = SizeF(s1.Width, imgSize.Width)
rect1 = RectangleF(PointF(x, y), size)
format = PdfStringFormat(PdfTextAlignment.Left, PdfVerticalAlignment.Middle)

# Draw the text1
page.Canvas.DrawString(text1, font, bursh, rect1, format)

# Draw the image
x += s1.Width
page.Canvas.DrawImage(image, PointF(x, y), imgSize)

# Draw the text2
x += imgSize.Width
size = SizeF(s2.Width, imgSize.Height)
rect1 = RectangleF(PointF(x, y), size)
page.Canvas.DrawString(text2, font, bursh, rect1, format)
```

---

# PDF Page Number in Footer
## Add page numbers to the footer of a PDF document
```python
def DrawPageNumber(doc, margin, startNumber, pageCount):
    for i in range(doc.Pages.Count):
        page = doc.Pages.get_Item(i)
        page.Canvas.SetTransparency(0.5)
        brush = PdfBrushes.get_Black()
        pen = PdfPen(brush, 0.75)
        font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Italic, True)
        format = PdfStringFormat(PdfTextAlignment.Right)
        format.MeasureTrailingSpaces = True
        space = font.Height * 0.75
        x = margin.Left
        width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
        y = page.Canvas.ClientSize.Height - margin.Bottom + space
        page.Canvas.DrawLine(pen, x, y, x + width, y)
        y = y + 1
        numberLabel = "{0:d} of {1:d}".format(startNumber, pageCount)
        startNumber += 1
        page.Canvas.DrawString(numberLabel, font, brush, x + width, y, format)
        page.Canvas.SetTransparency(1.0)
```

---

# Spire.PDF Invisible Signature
## Add an invisible digital signature to a PDF document
```python
# Create a signature maker object for the loaded document using the PFX file and password
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")

# Make the invisible signature with the specified name
signatureMaker.MakeSignature("signName")
```

---

# Spire.PDF Signature Validity
## Add validity check mark to signature in PDF document
```python
# Create a signature maker object for the document using the PFX file and password
signatureMaker = PdfOrdinarySignatureMaker(doc, "path_to_pfx_file", "password")

# Disable Acro6 layers in the signature
signatureMaker.SetAcro6Layers(False)

# Add the invisible signature to the first page of the document at the specified coordinates
signatureMaker.MakeSignature("signName", doc.Pages.get_Item(0), 100.0, 100.0, 120.0, 160.0)
```

---

# PDF Security Permission Management
## Change security permissions and encryption settings for a PDF document
```python
# Define the security policy for the document
# No user password is set, but an owner password "test" is used
securityPolicy = PdfPasswordSecurityPolicy("", "test")

# Set the encryption algorithm to AES with a 256-bit key length
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_256

# Define document privileges
dp = PdfDocumentPrivilege.ForbidAll()
dp.AllowDegradedPrinting = True
dp.AllowFillFormFields = True

# Assign the document privileges to the security policy
securityPolicy.DocumentPrivilege = dp

# Apply the security policy to the document
doc.Encrypt(securityPolicy)
```

---

# PDF Password Protection Check
## Check if a PDF document is password protected
```python
# Check if the document is password protected
isProtected = PdfDocument.IsPasswordProtected(inputFile)

# Determine the message based on whether the document is protected
word = "password " if isProtected else "not password "
stringBuilder = "The pdf is " + word + "protected!"
```

---

# PDF Document Decryption
## Demonstrates how to decrypt a password-protected PDF document
```python
# Load a PDF document from disk
doc = PdfDocument()

# Use 'test' as the owner password
doc.LoadFromFile("path_to_pdf_file","test")

# Decrypt the document
doc.Decrypt()

# # Or you can use 'open' as the user password
# doc.LoadFromFile("path_to_pdf_file","open")
# # Decrypt the document using the owner password
# doc.Decrypt("test")
```

---

# PDF Password Verification
## Check if a password can open a protected PDF document
```python
# Iterate through each password
for value in passwords:
    try:
        # Create a new PDF document
        doc = PdfDocument()
        # Load the PDF from file with the current password
        doc.LoadFromFile(inputFile,value)
        # If no exception is thrown, the password is correct
        stringBuilder+="Password = " + value + "  is correct" + "\n"
    except SpireException as e:
        # If an exception is thrown, the password is incorrect
        stringBuilder+="Password = " + value + "  is not correct"+ "\n"
```

---

# spire.pdf digital signature
## Create and apply digital signature to PDF document
```python
# Create a signature maker with the PDF document and PFX file
signatureMaker = PdfOrdinarySignatureMaker(doc, inputFile_pfx, "e-iceblue")

# Configure the signature properties
signature = signatureMaker.Signature
signature.Name = "Gary"
signature.ContactInfo = "028-81705109"
signature.Location = "Chengdu"
signature.Reason = "The certificate of this document"

# Create a signature appearance
appearance = PdfSignatureAppearance(signature)
appearance.NameLabel = "Signer: "
appearance.ContactInfoLabel = "ContactInfo: "
appearance.LocationLabel = "Location: "
appearance.ReasonLabel = "Reaseon: "
appearance.SignatureImage = PdfImage.FromFile(inputImage)
appearance.GraphicMode = GraphicMode.SignImageAndSignDetail
appearance.SignImageLayout = SignImageLayout.none

# Apply the signature to the PDF document
signatureMaker.MakeSignature("Signer:", doc.Pages.get_Item(0), 90.0, 550.0, 270.0, 90.0, appearance)
```

---

# PDF Document Encryption
## Demonstrates how to encrypt a PDF document with password protection and specific privileges
```python
# Create a PDF document
doc = PdfDocument()

# Create a security policy with user and owner passwords
securityPolicy = PdfPasswordSecurityPolicy("open", "test")

# Set the encryption algorithm
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.RC4_128

# Define document privileges
dp = PdfDocumentPrivilege.ForbidAll()
dp.AllowPrint = True
dp.AllowFillFormFields = True
securityPolicy.DocumentPrivilege = dp

# Encrypt the document with the security policy
doc.Encrypt(securityPolicy)
```

---

# Spire.PDF Extract Signature Images
## Extract images from PDF signatures and save them as files
```python
# Access the form in the document
pdfform = doc.Form

# Get the form widget
formWidget = PdfFormWidget(pdfform)
i = 0

# Extract signature images and save them to files
for image in formWidget.ExtractSignatureAsImages:
    filename = outputFile + "Image-" + str(i) + ".png"
    # Save the image to a file
    image.Save(filename)
    i = i + 1
```

---

# Spire.PDF Security Verification
## Check if a signed PDF document has been modified
```python
# Access the form in the PDF document
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)

modified = False

# Check if there are any form fields in the document
if formWidget.FieldsWidget.Count > 0:
    # Loop through each form field
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        # Verify that the field is a PdfField instance
        if isinstance(field, PdfField):
            # Convert the field to a signature field widget
            signatureField = PdfSignatureFieldWidget(field)
            # Get the signature object associated with the signature field
            signatureOne = signatureField.Signature
            # Verify if the document was modified
            modified = signatureOne.VerifyDocModified()
            break
```

---

# spire.pdf python encryption
## implement new encryption method for PDF documents
```python
# Create password security policy
securityPolicy = PdfPasswordSecurityPolicy("123456789", "M123456789")

# Set encryption algorithm
securityPolicy.EncryptionAlgorithm = PdfEncryptionAlgorithm.AES_128

# Set document permissions (ownership)
securityPolicy.DocumentPrivilege = PdfDocumentPrivilege.ForbidAll()

# Set printing permissions
securityPolicy.DocumentPrivilege.AllowPrint = True
pdfDocument.Encrypt(securityPolicy)
```

---

# spire.pdf python timestamp signature
## Create and configure a timestamped digital signature for a PDF document
```python
# Create a digital signature
signature = Security_PdfSignature(doc, doc.Pages.get_Item(0), inputFile_pfx, "e-iceblue", "signature")

# Set the bounds of the signature box
signature.Bounds = RectangleF(PointF(90.0, 550.0), SizeF(180.0, 90.0))

# Configure signature appearance and details
signature.NameLabel = "Digitally signed by:Gary"
signature.LocationInfoLabel ="Location:"
signature.LocationInfo = "CN"
signature.ReasonLabel = "Reaseon:"
signature.Reason = "Ensure authenticity"
signature.ContactInfoLabel = "Contact Number: "
signature.ContactInfo = "028-81705109"

# Set document permissions
signature.DocumentPermissions = PdfCertificationFlags.AllowFormFill.value | PdfCertificationFlags.ForbidChanges.value

# Set graphic mode for the signature
signature.GraphicsMode = Security_GraphicMode.SignImageAndSignDetail

# Set the signature image
signature.SignImageSource = PdfImage.FromFile(inputImage)

# Configure timestamp URL
url = "https://freetsa.org/tsr"
signature.ConfigureTimestamp(url)
```

---

# spire.pdf python signature verification
## verify signatures in a PDF document
```python
# Load a Pdf document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Access the form in the document
pdfform = doc.Form
formWidget = PdfFormWidget(pdfform)

# Check if there are any form fields in the document
if formWidget.FieldsWidget.Count > 0:
    # Loop through each form field
    for i in range(formWidget.FieldsWidget.Count):
        field = formWidget.FieldsWidget.get_Item(i)
        # Verify that the field is a PdfField instance
        if isinstance(field, PdfField):
            # Convert the field to a signature field widget
            signatureField = PdfSignatureFieldWidget(field)
            # Get the full name of the signature field
            fullName = signatureField.FullName
            # Verify the signature
            valid = doc.VerifySignature(fullName)
```

---

# Spire.PDF Python Launch Action
## Add PDF launch action to document
```python
#Create a new PDF document
doc = PdfDocument()
page = doc.Pages.Add()
#Create a PDF Launch Action       
launchAction = PdfLaunchAction(inputFile)
#Create a PDF Action Annotation with the PDF Launch Action
text = "Click here to open file"
font = PdfTrueTypeFont("Arial", 13.0,PdfFontStyle.Regular,True)
rect = RectangleF(50.0, 50.0, 230.0, 15.0)
page.Canvas.DrawString(text, font, PdfBrushes.get_ForestGreen(), rect)
annotation = PdfActionAnnotation(rect, launchAction)
#Add the PDF Action Annotation to page
newPage = PdfNewPage(page.Ptr)
newPage.Annotations.Add(annotation)
```

---

# spire.pdf table of contents
## add table of contents to pdf document
```python
#insert a blank page into the pdf document
tocPage = doc.Pages.Insert(0)
#set title
title = "Table Of Contents"
titleFont = PdfTrueTypeFont("Arial", 20.0, PdfFontStyle.Bold, True)
centerAlignment = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
location = PointF(tocPage.Canvas.ClientSize.Width / float(2), titleFont.MeasureString(title).Height)
tocPage.Canvas.DrawString(title, titleFont, PdfBrushes.get_CornflowerBlue(), location, centerAlignment)
#draw TOC text
titlesFont = PdfTrueTypeFont("Arial", 14.0,PdfFontStyle.Regular,True)
titles = [None for _ in range(pageCount)]
i = 0
while i < len(titles):
    titles[i] = "This is page{0:d}".format(i+1)
    i += 1
y = titleFont.MeasureString(title).Height + 10
x = 0.0
newPage = PdfNewPage(tocPage.Ptr)
for i in range(1, pageCount + 1):
    text = titles[i-1]
    titleSize = titlesFont.MeasureString(text)
    navigatedPage = doc.Pages[i]
    pageNumText = str((i+1))
    pageNumTextSize = titlesFont.MeasureString(pageNumText)
    tocPage.Canvas.DrawString(text, titlesFont, PdfBrushes.get_CadetBlue(), 0.0, y)
    dotLocation = titleSize.Width + 2 + x
    pageNumlocation = tocPage.Canvas.ClientSize.Width - pageNumTextSize.Width
    while dotLocation < pageNumlocation :
        if dotLocation >= pageNumlocation:
            break
        tocPage.Canvas.DrawString(".", titlesFont, PdfBrushes.get_Gray(), dotLocation, y)
        dotLocation += 3
    tocPage.Canvas.DrawString(pageNumText, titlesFont, PdfBrushes.get_CadetBlue(), pageNumlocation, y)
    #add TOC action
    location = PointF(0.0, y)
    titleBounds = RectangleF(location, SizeF(tocPage.Canvas.ClientSize.Width, titleSize.Height))
    Dest = PdfDestination(navigatedPage, PointF(-doc.PageSettings.Margins.Top, -doc.PageSettings.Margins.Left))
    gotoAction = PdfGoToAction(Dest)
    action = PdfActionAnnotation(titleBounds, gotoAction)
    action.Border = PdfAnnotationBorder(0.0)
    newPage.Annotations.Add(action)
    y += titleSize.Height + 10
```

---

# PDF Document Link Annotation
## Create a document link annotation in PDF that links to another page within the same document
```python
def AddDocumentLinkAnnotation(pdf, AddPage, DestinationPage, y):
    #Define a font
    font = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Regular, True)
    #Set the string format
    format = PdfStringFormat(PdfTextAlignment.Left)
    #Text string
    prompt = "Local document Link: "
    #Draw text string on page
    pdf.Pages[AddPage].Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
    #Use MeasureString to get the width of string
    x = font.MeasureString(prompt, format).Width
    #Create a PdfDestination with specific page
    dest = PdfDestination(pdf.Pages[DestinationPage])
    #Set the location of destination
    dest.Location = PointF(0.0, y)
    #Set 50% zoom factor
    dest.Zoom = 0.5
    #Label string
    label = "Click here to link the second page."
    #Use MeasureString to get the SizeF of string
    size = font.MeasureString(label)
    #Create a rectangle
    bounds = RectangleF(x, y, size.Width, size.Height)
    #Draw label string
    pdf.Pages[AddPage].Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
    #Create PdfDocumentLinkAnnotation on the rectangle and link to the destination  
    annotation = PdfDocumentLinkAnnotation(bounds, dest)
    #Set color for annotation
    annotation.Color = PdfRGBColor(Color.get_Blue())
    #Add annotation to the page
    addPage = pdf.Pages[AddPage]
    newPage = PdfNewPage(addPage.Ptr)
    newPage.Annotations.Add(annotation)

#Create a pdf document
doc = PdfDocument()
#Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
#Setting for page margin
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(2.0, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
#Add the first page
page1 = doc.Pages.Add(PdfPageSize.A4(), margin)
#Define a PdfBrush
brush1 = PdfBrushes.get_Black()
#Define a font
font1 = PdfTrueTypeFont("Arial", 12.0, PdfFontStyle.Bold, True)
#Set the string format 
format1 = PdfStringFormat(PdfTextAlignment.Left)
#Set the position for drawing 
x = 0.0
y = 50.0
#Text string 
specification = "The sample demonstrates how to create a local document link in PDF document."
#Draw text string on first page 
page1.Canvas.DrawString(specification, font1, brush1, x, y, format1)
#Use MeasureString to get the height of string
y = y + font1.MeasureString(specification, format1).Height +10
#Add the second page
page2 = doc.Pages.Add(PdfPageSize.A4(), margin)
#String text
PageContent = "This is the second page!"
#Draw text string on second page 
page2.Canvas.DrawString(PageContent, font1, brush1, x, y, format1)
#Add DocumentLinkAnnotation on the first page and link to the second page
AddDocumentLinkAnnotation(doc, 0, 1, y)
```

---

# PDF Sound Embedding
## Embed sound files in PDF documents
```python
# Create a sound action
soundAction = PdfSoundAction(inputFile2)
soundAction.Sound.Bits = 15
soundAction.Sound.Channels = PdfSoundChannels.Stereo
soundAction.Sound.Encoding = PdfSoundEncoding.Signed
soundAction.Volume = 0.8
soundAction.Repeat = True
# Set the sound action to be executed when the PDF document is opened
doc.AfterOpenAction = soundAction
```

---

# Spire.PDF for Python - Extract and Update Links
## Extract and update web link annotations in a PDF document
```python
#Get the first page
page = doc.Pages[0]
#Get the annotation collection
widgetCollection = page.AnnotationsWidget
#Verify whether widgetCollection is null or not
if widgetCollection.Count > 0:
    for i in range(widgetCollection.Count):
        annotation = widgetCollection.get_Item(i)
        #Get the TextWebLink Annotation
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            #Get the link annotation
            link = annotation if isinstance(annotation, PdfTextWebLinkAnnotationWidget) else None
            #Change the url
            link.Url = "http://www.e-iceblue.com/Introduce/pdf-for-net-introduce.html"
```

---

# PDF File Link Annotation
## Create a file link annotation in a PDF document
```python
def AddFileLinkAnnotation(page, y, inputFile):
    #Define a font
    font = PdfTrueTypeFont("Arial", 12.0,PdfFontStyle.Regular,True)
    #Set the string format 
    format = PdfStringFormat(PdfTextAlignment.Left)
    #Text string
    prompt = "Launch a File: "
    #Draw text string on page canvas
    page.Canvas.DrawString(prompt, font, PdfBrushes.get_DodgerBlue(), 0.0, y)
    #Use MeasureString to get the width of string
    x = font.MeasureString(prompt, format).Width
    #String of file name
    label = "Sample.pdf"
    #Use MeasureString to get the SizeF of string
    size = font.MeasureString(label)
    #Create a rectangle
    bounds = RectangleF(x, y, size.Width, size.Height)
    #Draw label string
    page.Canvas.DrawString(label, font, PdfBrushes.get_OrangeRed(), x, y)
    #Create PdfFileLinkAnnotation on the rectangle and link file "Sample.pdf"
    annotation = PdfFileLinkAnnotation(bounds, inputFile)
    #Set color for annotation
    annotation.Color = PdfRGBColor(Color.get_Blue())
    #Add annotation to the page
    newPage = PdfNewPage(page.Ptr)
    newPage.Annotations.Add(annotation)
```

---

# Spire.PDF Python Get Link Annotation
## Extract web link annotations from a PDF document
```python
#Create a pdf document
doc = PdfDocument()
#Get the first page
page = doc.Pages[0]
#Get the annotation collection
annotations = page.AnnotationsWidget
#Create list to save results
content = []
#Verify whether widgetCollection is not null or not
if annotations.Count > 0:
    #traverse the PdfAnnotationCollection
    for i in range(annotations.Count):
        annotation = annotations.get_Item(i)
        #if it is PdfTextWebLinkAnnotationWidget
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            #Get the Url
            WebLinkAnnotation = annotation if isinstance(annotation, PdfTextWebLinkAnnotationWidget) else None
            url = WebLinkAnnotation.Url
            #Add strings to content list
            content.append("The url of link annotation is "+ url+"\r\n")
            content.append("The text of link annotation is " + WebLinkAnnotation.Text)
```

---

# Spire.PDF Python GoTo Actions
## Create embedded and location-specific GoTo actions in PDF documents

## Create Embedded GoTo Action
```python
def EmbeddedGoToAction(pdf, page, newPage):
    # Add text for the action
    text = "Test embedded go-to action! Click this will open the attached PDF in a new window."
    font = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Regular, True)
    width = 490.0
    height = font.Height * 2.2
    rect = RectangleF(0.0, 100.0, width, height)
    page.Canvas.DrawString(text, font, PdfBrushes.get_Black(), rect)
    
    # Create a PdfDestination with specific page, location and 200% zoom factor
    dest = PdfDestination(1, PointF(0.0, 842.0), 2.0)
    # Create GoToE action with dest
    action = PdfEmbeddedGoToAction("sample.pdf", dest, True)
    annotation = PdfActionAnnotation(rect, action)
    # Add the annotation
    newPage.Annotations.Add(annotation)
```

## Create Jump to Specific Location Action
```python
def JumpToSpecificLocationAction(pdf, page, newPage):
    # Add a new page
    pagetwo = pdf.Pages.Add()
    # Draw text on the page
    pagetwo.Canvas.DrawString("This is Page Two.", PdfFont(PdfFontFamily.Helvetica, 20.0), 
                             PdfSolidBrush(PdfRGBColor(Color.get_Black())), 10.0, 10.0)
    
    # Create PdfDestination instance and link to PdfGoToAction
    pageBottomDest = PdfDestination(pagetwo)
    pageBottomDest.Location = PointF(0.0, 5.0)
    pageBottomDest.Mode = PdfDestinationMode.Location
    pageBottomDest.Zoom = 1.0
    action = PdfGoToAction(pageBottomDest)
    
    # Create button for the action
    buttonFont = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Bold, True)
    buttonWidth = 70.0
    buttonHeight = buttonFont.Height * 1.5
    format2 = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    buttonBounds = RectangleF(0.0, 200.0, buttonWidth, buttonHeight)
    
    # Create button appearance
    page.Canvas.DrawRectangle(PdfBrushes.get_DarkGray(), buttonBounds)
    page.Canvas.DrawString("To Last Page", buttonFont, PdfBrushes.get_CadetBlue(), buttonBounds, format2)
    
    # Add the annotation
    annotation = PdfActionAnnotation(buttonBounds, action)
    annotation.Border = PdfAnnotationBorder(0.75)
    annotation.Color = PdfRGBColor(Color.get_LightGray())
    newPage.Annotations.Add(annotation)
```

---

# Spire.PDF Launch File in New Window
## Create a PDF action annotation that launches a file in a new window
```python
# Create launch action to open file in new window
launchAction = PdfLaunchAction(file_path, PdfFilePathType.Relative)
launchAction.IsNewWindow = True

# Add annotation to the PDF
rect = RectangleF(x, y, width, height)
annotation = PdfActionAnnotation(rect, launchAction)
pageWidget = PdfPageWidget(page)
pageWidget.AnnotationsWidget.Add(annotation)
```

---

# Spire.PDF Python Links
## Create different types of links in PDF documents
```python
# Font setup
font = PdfTrueTypeFont("Lucida Sans Unicode", 14.0, PdfFontStyle.Regular, True)
font1 = PdfTrueTypeFont("Lucida Sans Unicode", 14.0, PdfFontStyle.Underline, True)
format = PdfStringFormat()
format.MeasureTrailingSpaces = True

# Simple text link
url1 = "http://www.e-iceblue.com"
page.Canvas.DrawString("Simple Text Link: ", font, PdfBrushes.get_Orange(), 0.0, y, format)
x = font.MeasureString("Simple Text Link: ", format).Width
page.Canvas.DrawString(url1, font1, PdfBrushes.get_CadetBlue(), x, y)

# Web link using PdfTextWebLink
webLink = PdfTextWebLink()
webLink.Text = "E-iceblue home"
webLink.Url = url1
webLink.Font = font1
webLink.Brush = PdfBrushes.get_CadetBlue()
webLink.DrawTextWebLink(page.Canvas, PointF(x, y))

# URI annotation
text = "Google"
location = PointF(x, y)
size = font1.MeasureString(text)
linkBounds = RectangleF(location, size)
uriAnnotation = PdfUriAnnotation(linkBounds)
uriAnnotation.Border = PdfAnnotationBorder(0.0)
uriAnnotation.Uri = "http://www.google.com"
newPage.Annotations.Add(uriAnnotation)
page.Canvas.DrawString(text, font1, PdfBrushes.get_CadetBlue(), x, y)

# URI annotation with JavaScript action
text = "JavaScript Action (Click Me)"
location = PointF(x-2, y-2)
size = font1.MeasureString(text)
size = SizeF(size.Width+5, size.Height+5)
linkBounds = RectangleF(location, size)
jsAnnotation = PdfUriAnnotation(linkBounds)
jsAnnotation.Border = PdfAnnotationBorder(0.75)
jsAnnotation.Color = PdfRGBColor(Color.get_CadetBlue())
script = "app.alert({cMsg: \"Hello.\", nIcon: 3, cTitle: \"JavaScript Action\"});"
action = PdfJavaScriptAction(script)
jsAnnotation.Action = action
newPage.Annotations.Add(jsAnnotation)
page.Canvas.DrawString(text, font1, PdfBrushes.get_CadetBlue(), x, y)

# Forum and email links using PdfTextWebLink
forumLink = PdfTextWebLink()
forumLink.Text = "Go to forum to ask questions"
forumLink.Url = "https://www.e-iceblue.com/forum/components-f5.html"
forumLink.Font = font1
forumLink.Brush = PdfBrushes.get_CadetBlue()
forumLink.DrawTextWebLink(page.Canvas, PointF(x, y))

emailLink = PdfTextWebLink()
emailLink.Text = "Send an email"
emailLink.Url = "mailto:support@e-iceblue.com"
emailLink.Font = font1
emailLink.Brush = PdfBrushes.get_CadetBlue()
emailLink.DrawTextWebLink(page.Canvas, PointF(x, y))
```

---

# Spire.PDF Remove Open Action
## Remove the open action from a PDF document
```python
# Create a pdf document
document = PdfDocument()
# Remove action
document.AfterOpenAction = None
```

---

# Spire.PDF Python Page Navigation
## Specify page to view when opening PDF
```python
#Create a pdf document
doc = PdfDocument()
#Create a PdfDestination with specific page, location and 50% zoom factor
dest = PdfDestination(2, PointF(0.0, 100.0), 0.5)
#Create GoToAction with dest
action = PdfGoToAction(dest)
#Set open action
doc.AfterOpenAction = action
```

---

# Spire.PDF Python Attachment Management
## Add attachments to a PDF document
```python
# Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile1)
# Load files and add in attachments
data = Stream(inputFileImg)
attach1 = PdfAttachment("attachment1.png", data)
data2 = Stream(inputFile2)
attach2 = PdfAttachment("attachment2.pdf", data2)
doc.Attachments.Add(attach1)
doc.Attachments.Add(attach2)
doc.SaveToFile(outputFile, FileFormat.PDF)
doc.Close()
```

---

# Spire.PDF grayscale conversion
## Convert PDF to grayscale
```python
# Create a PdfGrayConverter with a PDF file
converter = PdfGrayConverter(inputFile)
# Convert the file to grayscale PDF
converter.ToGrayPdf(outputFile)
```

---

# Spire.PDF Python Conversion
## Convert PDF document to OFD format
```python
inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ConvertToOFD.ofd"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Convert pdf to ofd
doc.SaveToFile(outputFile, FileFormat.OFD)
doc.Close()
```

---

# PDF to Word Conversion with Document Properties
## Convert PDF to Word document and set various document properties
```python
inputFile = "./Demos/Data/Sample.pdf"
outputFile = "ConvertToWordSettingProperties-result.docx"
#Create PdfToDocConverter
converter = PdfToDocConverter(inputFile)
#Set properties for the .docx document
converter.DocxOptions.Title = "PDFTODOCX"
converter.DocxOptions.Subject = "Set document properties."
converter.DocxOptions.Tags = "Test Tags"
converter.DocxOptions.Categories = "PDF"
converter.DocxOptions.Commments = "This document is just for testing the properties"
converter.DocxOptions.Authors = "E-iceblue Support Team"
converter.DocxOptions.LastSavedBy = "E-iceblue Support Team"
converter.DocxOptions.Revision = 8
converter.DocxOptions.Version = "csharp V4.0"
converter.DocxOptions.ProgramName = "Spire.Pdf for .NET"
converter.DocxOptions.Company = "E-iceblue"
converter.DocxOptions.Manager = "E-iceblue"
#Convert to docx file
converter.SaveToDocx(outputFile)
```

---

# Spire.PDF PDF/A to PDF Conversion
## Convert PDF/A documents to standard PDF format
```python
# Open pdf document
doc = PdfDocument()
# Create a new pdf and draw content on new file
newDoc = PdfNewDocument()
newDoc.CompressionLevel = PdfCompressionLevel.none
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    size = page.Size
    p = newDoc.Pages.Add(size, PdfMargins(0.0))
    page.CreateTemplate().Draw(p, 0.0, 0.0)
```

---

# spire.pdf python conversion
## convert PDF to Excel format
```python
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save the pdf file to excel
pdf.SaveToFile(outputFile, FileFormat.XLSX)
pdf.Close()
```

---

# spire.pdf python conversion
## convert PDF to Excel with specific options
```python
# Create a PDF document object
pdf = PdfDocument()
# Load the PDF file
pdf.LoadFromFile(inputFile)
# Set PDF to Excel conversion options
pdf.ConvertOptions.SetPdfToXlsxOptions(
    XlsxLineLayoutOptions(False, True, True))
# Save the PDF file to Excel format
pdf.SaveToFile(outputFile, FileFormat.XLSX)
pdf.Close()
```

---

# Remove hyperlinks from PDF
## Remove TextWebLink annotations from a PDF document
```python
# Get the first page
page = document.Pages[0]
# Get the annotation collection
widgetCollection = page.AnnotationsWidget
# Verify whether widgetCollection is null or not
if widgetCollection.Count > 0:
    for i in range(widgetCollection.Count - 1, -1, -1):
        annotation = widgetCollection.get_Item(i)
        # Get the TextWebLink Annotation
        if isinstance(annotation, PdfTextWebLinkAnnotationWidget):
            link = annotation if isinstance(
                annotation, PdfTextWebLinkAnnotationWidget) else None
            # Remove the TextWebLink annotation
            widgetCollection.Remove(link)
```

---

# Spire.PDF SVG to PDF Conversion
## Convert SVG files to PDF format using Spire.PDF library
```python
# Create a new PDF document
doc = PdfDocument()
# Load the SVG file
doc.LoadFromSvg(inputFile)
# Save the document as PDF
doc.SaveToFile(outputFile)
doc.Close()
```

---

# Spire.PDF Text to PDF Conversion
## Core functionality for converting text to PDF document using Spire.PDF
```python
# Create a pdf document
doc = PdfDocument()
section = doc.Sections.Add()
page = section.Pages.Add()
# Create a PdfFont
font = PdfFont(PdfFontFamily.Helvetica, 11.0)
# Set string format
strformat = PdfStringFormat()
strformat.LineSpacing = 20.0
brush = PdfBrushes.get_Black()
# Set text layout
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(10.0, 20.0), page.Canvas.ClientSize)
textWidget = PdfTextWidget(text, font, brush)
textWidget.StringFormat = strformat
textWidget.Draw(page, bounds, textLayout)
```

---

# Spire.PDF PDF to DOC Conversion
## Convert PDF document to DOC format
```python
# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.DOC)
doc.Close()
```

---

# PDF to DOCX Conversion
## Convert PDF document to DOCX format using Spire.PDF
```python
# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputfile)
# Convert to doc file.
doc.SaveToFile(outputFile, FileFormat.DOCX)
doc.Close()
```

---

# PDF to HTML Conversion
## Convert PDF document to HTML format using Spire.PDF
```python
# Create a PDF document
doc = PdfDocument()
# Load the PDF file
doc.LoadFromFile(inputFile)
# Convert to HTML format
doc.SaveToFile(outputFile, FileFormat.HTML)
# Close the document
doc.Close()
```

---

# PDF to Image Conversion
## Convert PDF pages to images using Spire.PDF
```python
# Open pdf document
doc = PdfDocument()

# Convert each page to image
for i in range(doc.Pages.Count):
    doc.SaveAsImage(i)

doc.Close()
```

---

# Spire.PDF Linearized PDF Conversion
## Convert PDF to linearized PDF format for faster web viewing
```python
# Create PDF to linearized PDF converter
converter = PdfToLinearizedPdfConverter(inputFile)
# Convert the PDF to linearized format
converter.ToLinearizedPdf(outputFile)
```

---

# PDF to PCL Conversion
## Convert PDF document to PCL format using Spire.PDF
```python
inputFile = "./Demos/Data/ToPCL.pdf"
outputFile = "ToPCL.pcl"

# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to PCL file.
doc.SaveToFile(outputFile, FileFormat.PCL)
doc.Close()
```

---

# PDF to PDF/A Conversion
## Convert PDF file to PDF/A-1b standard format
```python
# Convert to PDFA file
converter = PdfStandardsConverter(inputFile)
converter.ToPdfA1B(outputFile)
```

---

# Spire.PDF PDF/A2B Conversion
## Convert PDF to PDF/A2B format
```python
# Convert to PDFA file
converter = PdfStandardsConverter(inputFile)
# also supports ToPdfA1B ToPdfA1A ToPdfA2A ToPdfA3A ToPdfA3B ToPdfX1A2001
converter.ToPdfA2B(outputFile)
```

---

# Spire.PDF PostScript Conversion
## Convert PDF to PostScript format
```python
# Create a PDF document object
doc = PdfDocument()
# Load a PDF document
doc.LoadFromFile(inputFile)
# Convert to PostScript file
doc.SaveToFile(outputFile, FileFormat.POSTSCRIPT)
doc.Close()
```

---

# spire.pdf python to pptx conversion
## Convert PDF document to PPTX format
```python
# Create PDF document
pdf = PdfDocument()
# Load PDF file
pdf.LoadFromFile(inputFile)
# Save the PDF file to PPTX
pdf.SaveToFile(outputFile, FileFormat.PPTX)
pdf.Close()
```

---

# Spire.PDF Python Conversion
## Convert PDF to SVG
```python
# Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Convert to SVG file.
doc.SaveToFile(outputFile, FileFormat.SVG)
doc.Close()
```

---

# PDF to Transparent Background Image Conversion
## Convert PDF page to transparent background image
```python
# Define file paths
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
```

---

# Spire.PDF to XLSX Conversion
## Convert PDF document to XLSX format
```python
# Create a PDF document object
pdf = PdfDocument()
# Load the PDF file
pdf.LoadFromFile(inputFile)
# Save the PDF file to Excel format
pdf.SaveToFile(outputFile, FileFormat.XLSX)
# Close the PDF document
pdf.Close()
```

---

# PDF to XPS Conversion
## Convert PDF document to XPS format
```python
pdf = PdfDocument()
pdf.LoadFromFile(inputFile)
# Save the pdf file to xps
pdf.SaveToFile(outputFile, FileFormat.XPS)
pdf.Close()
```

---

# Spire.PDF PDF to HTML with Embedded Images
## Convert PDF to HTML with embedded images option
```python
# Open pdf document
doc = PdfDocument()
# Set the conversion option to embed image in html
doc.ConvertOptions.SetPdfToHtmlOptions(True, True)
# Convert to html file
doc.SaveToFile(outputFile, FileFormat.HTML)
doc.Close()
```

---

# PDF to HTML Conversion with Embedded SVG
## Convert PDF document to HTML format with SVG embedding option
```python
# Open PDF document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
# Set the conversion option to embed image in HTML
doc.ConvertOptions.SetPdfToHtmlOptions(True)
# Convert to HTML file
doc.SaveToFile(outputFile, FileFormat.HTML)
doc.Close()
```

---

# Spire.PDF Python Conversion
## Set PDF to HTML conversion options with embedded images
```python
#Set the convertion option to embed image in html
doc.ConvertOptions.SetPdfToHtmlOptions(False, True, 1)
```

---

# Spire.PDF Python Conversion
## Convert PDF to HTML stream
```python
inputFile = "./Demos/Data/Sample.pdf"
outputFile = "oHTMLStream.html"

#Open pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Save to HTML stream
fileStream = Stream(outputFile)
doc.SaveToStream(fileStream, FileFormat.HTML)
fileStream.Close()
```

---

# spire.pdf python delete page
## delete a specific page from a PDF document
```python
# Delete the fifth page (index 4)
doc.Pages.RemoveAt(4)
```

---

# PDF Content Extraction
## Extract text and images from PDF pages
```python
# Iterate through each page in the document
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)

    # Extract text from the page
    pdfTextExtractor = PdfTextExtractor(page)
    pdfTextExtractOptions = PdfTextExtractOptions()
    pdfTextExtractor.ExtractText(pdfTextExtractOptions)
    
    # Extract images from the page
    imageHelper = PdfImageHelper()
    imageInfo = imageHelper.GetImagesInfo(page)
    for info in imageInfo:
        info.Image
```

---

# Spire.PDF Page Count
## Get the number of pages in a PDF document
```python
# Load the document from disk
doc = PdfDocument()
doc.LoadFromFile(inputFile)
count = doc.Pages.Count
doc.Close()
```

---

# PDF Page Information Extraction
## Extract various dimensions and properties of a PDF page
```python
# Create a pdf document
doc = PdfDocument()
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the size of page MediaBox based on "point"
MediaBoxWidth = page.MediaBox.Width
MediaBoxHeight = page.MediaBox.Height
MediaBoxX = page.MediaBox.X
MediaBoxY = page.MediaBox.Y
# Get the size of page BleedBox based on "point"
BleedBoxWidth = page.BleedBox.Width
BleedBoxHeight = page.BleedBox.Height
BleedBoxX = page.BleedBox.X
BleedBoxY = page.BleedBox.Y
# Get the size of page CropBox based on "point"
CropBoxWidth = page.CropBox.Width
CropBoxHeight = page.CropBox.Height
CropBoxX = page.CropBox.X
CropBoxY = page.CropBox.Y
# Get the size of page ArtBox based on "point"
ArtBoxWidth = page.ArtBox.Width
ArtBoxHeight = page.ArtBox.Height
ArtBoxX = page.ArtBox.X
ArtBoxY = page.ArtBox.Y
# Get the size of page TrimBox based on "point"
TrimBoxWidth = page.TrimBox.Width
TrimBoxHeight = page.TrimBox.Height
TrimBoxX = page.TrimBox.X
TrimBoxY = page.TrimBox.Y
# Get the actual size of page
actualSizeW = page.ActualSize.Width
actualSizeH = page.ActualSize.Height
# Gets the rotation angle of the current page
rotationAngle = page.Rotation
rotation = str(rotationAngle)
```

---

# PDF Page Label Extraction
## Extract page labels from a PDF document
```python
# Create a PdfDocument instance
pdf = PdfDocument()
# Load the PDF file
pdf.LoadFromFile(file_path)
# Get the labels of the pages in the PDF file
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)
    page_label = page.PageLabel
pdf.Close()
```

---

# Spire.PDF Page Size Extraction
## Extract PDF page size in different units
```python
# Create a pdf document
doc = PdfDocument()
# Load an existing pdf from disk
doc.LoadFromFile("path_to_pdf_file")
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the width of page based on "point"
pointWidth = page.Size.Width
# Get the height of page
pointHeight = page.Size.Height
# Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
# Convert the size with "pixel"
pixelWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Pixel)
pixelHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Pixel)
# Convert the size with "inch"
inchWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Inch)
inchHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Inch)
# Convert the size with "centimeter"
centimeterWidth = unitCvtr.ConvertUnits(
    pointWidth, PdfGraphicsUnit.Point, PdfGraphicsUnit.Centimeter)
centimeterHeight = unitCvtr.ConvertUnits(
    pointHeight, PdfGraphicsUnit.Point, PdfGraphicsUnit.Centimeter)
# Close the document
doc.Close()
```

---

# Spire.PDF Page Insertion
## Insert an empty page into a PDF document
```python
# Insert a blank page as the second page
doc.Pages.Insert(1)
```

---

# Spire.PDF Python Page Operations
## Insert an empty page at the end of a PDF document
```python
# Add an empty page at the end
doc.Pages.Add(PdfPageSize.A4(), PdfMargins(0.0, 0.0))
```

---

# Spire.PDF Page Labels
## Add page labels to PDF document
```python
# Create page labels
doc.PageLabels = PdfPageLabels()
doc.PageLabels.AddRange(
    0, PdfPageLabels.Decimal_Arabic_Numerals_Style(), "label test")
```

---

# Spire.PDF Page Setup
## Demonstrates various page setup options in PDF documents including page size, margins, orientation, rotation, and background color
```python
# Create a pdf document
doc = PdfDocument()
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create one page
page = doc.Pages.Add(PdfPageSize.A4(), margin)
page.BackgroundColor = Color.get_Chocolate()

page = doc.Pages.Add(PdfPageSize.A4(), margin)
page.BackgroundColor = Color.get_Coral()

page = doc.Pages.Add(PdfPageSize.A3(
), margin, PdfPageRotateAngle.RotateAngle180, PdfPageOrientation.Landscape)
page.BackgroundColor = Color.get_LightPink()

# create section
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin

# Set background color
page = section.Pages.Add()
page.BackgroundColor = Color.get_LightSkyBlue()

# Landscape
section = doc.Sections.Add()
section.PageSettings.Orientation = PdfPageOrientation.Landscape
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin

# Rotate 90
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle90

# Rotate 180
section = doc.Sections.Add()
page = section.Pages.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle180
```

---

# Spire.PDF Python Pagination
## Create a PDF document with pagination, including cover page, content pages, headers, footers, and page numbers
```python
def DrawCover(section, margin):
    section.PageSettings.Size = PdfPageSize.A4()
    section.PageSettings.Margins.All = 0.0
    page = section.Pages.Add()
    DrawPageHeaderAndFooter(page, margin, True)
    # Reference content
    brush1 = PdfBrushes.get_LightGray()
    brush2 = PdfBrushes.get_Blue()
    font1 = PdfTrueTypeFont("Arial", 8.0, PdfFontStyle.Regular, True)
    format = PdfStringFormat()
    format.MeasureTrailingSpaces = True
    text1 = "(All text and picture from "
    text2 = "Wikipedia"
    text3 = ", the free encyclopedia)"
    x = 0.0
    y = 10.0
    x = x + margin.Left
    y = y + margin.Top
    page.Canvas.DrawString(text1, font1, brush1, x, y, format)
    x = x + font1.MeasureString(text1, format).Width
    page.Canvas.DrawString(text2, font1, brush2, x, y, format)
    x = x + font1.MeasureString(text2, format).Width
    page.Canvas.DrawString(text3, font1, brush1, x, y, format)
    # Cover title
    brush3 = PdfBrushes.get_Black()
    format.Alignment = PdfTextAlignment.Center
    font2 = PdfTrueTypeFont("Arial", 24.0, PdfFontStyle.Bold, True)
    x = page.Canvas.ClientSize.Width / float(2)
    y = y + 100  # Adjusted y position for title
    page.Canvas.DrawString("Science History and Etymology",
                           font2, brush3, x, y, format)

def DrawContent(section, margin):
    section.PageSettings.Size = PdfPageSize.A4()
    section.PageSettings.Margins.All = 0.0
    page = section.Pages.Add()
    DrawPageHeaderAndFooter(page, margin, False)
    x = margin.Left
    y = margin.Top + 8
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    font1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Regular,  True)
    brush1 = PdfBrushes.get_Black()
    pen1 = PdfPen(brush1, 0.75)
    page.Canvas.DrawString(
        "Science History and Etymology", font1, brush1, x, y)
    y = y + font1.MeasureString("Science History and Etymology").Height + 6
    page.Canvas.DrawLine(
        pen1, x, y, page.Canvas.ClientSize.Width - margin.Right, y)
    y = y + 1.75
    font2 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Italic, True)
    format1 = PdfStringFormat()
    format1.MeasureTrailingSpaces = True
    format1.LineSpacing = font2.Height * 1.5
    format1.ParagraphIndent = font2.MeasureString("\t", format1).Width
    y = y + font2.Height * 0.5
    # Draw sample text
    page.Canvas.DrawString("This is a sample paragraph in italic style.", font2, brush1,
                           RectangleF(PointF(x, y), SizeF(width, 100)), format1)
    y = y + 50  # Approximate height of the paragraph
    font3 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
    format2 = PdfStringFormat()
    format2.LineSpacing = font3.Height * 1.4
    format2.MeasureTrailingSpaces = True
    # Draw more sample text
    page.Canvas.DrawString("This is a regular paragraph with more content.", font3, brush1,
                           RectangleF(PointF(x, y), SizeF(width, 100)), format2)
    y = y + 50  # Approximate height of the paragraph
    y = y + font3.Height * 0.75
    indent = font3.MeasureString("\t\t", format2).Width
    x1 = x + indent
    # Draw indented paragraph
    page.Canvas.DrawString("This is an indented paragraph with additional text content.", font3, brush1,
                           RectangleF(PointF(x1, y), SizeF(width - indent, 100)), format2)
    y = y + 50  # Approximate height of the paragraph
    y = y + font3.Height * 0.75
    # Simulate pagination by adding a new page when content exceeds page height
    if y > (page.Canvas.ClientSize.Height - margin.Bottom - 50):
        page = section.Pages.Add()
        DrawPageHeaderAndFooter(page, margin, False)
        y = margin.Top

def DrawPageHeaderAndFooter(page, margin, isCover):
    page.Canvas.SetTransparency(0.5)
    if isCover:
        page.Canvas.SetTransparency(1.0)
        return
    brush = PdfBrushes.get_Black()
    pen = PdfPen(brush, 0.75)
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(PdfTextAlignment.Right)
    format.MeasureTrailingSpaces = True
    space = font.Height * 0.75
    x = margin.Left
    width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
    y = margin.Top - space
    page.Canvas.DrawLine(pen, x, y, x + width, y)
    y = y - 1 - font.Height
    page.Canvas.DrawString("Demo of Spire.Pdf", font,
                           brush, x + width, y, format)
    page.Canvas.SetTransparency(1.0)

def DrawPageNumber(section, margin, startNumber, pageCount):
    for i in range(section.Pages.Count):
        page = section.Pages.get_Item(i)
        page.Canvas.SetTransparency(0.5)
        brush = PdfBrushes.get_Black()
        pen = PdfPen(brush, 0.75)
        font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
        format = PdfStringFormat(PdfTextAlignment.Right)
        format.MeasureTrailingSpaces = True
        space = font.Height * 0.75
        x = margin.Left
        width = page.Canvas.ClientSize.Width - margin.Left - margin.Right
        y = page.Canvas.ClientSize.Height - margin.Bottom + space
        page.Canvas.DrawLine(pen, x, y, x + width, y)
        y = y + 1
        numberLabel = "{0:d} of {1:d}".format(startNumber, pageCount)
        startNumber += 1
        page.Canvas.DrawString(numberLabel, font, brush, x + width, y, format)
        page.Canvas.SetTransparency(1.0)


# Create a pdf document
doc = PdfDocument()
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
DrawCover(doc.Sections.Add(), margin)
DrawContent(doc.Sections.Add(), margin)
DrawPageNumber(doc.Sections.get_Item(1), margin,
               1, doc.Sections.get_Item(1).Pages.Count)
```

---

# PDF Page Size Reset
## Reset PDF page dimensions by scaling and copying content
```python
# Set the margins
margins = PdfMargins(0.0)
# Create a new pdf document
with PdfDocument() as newDoc:
    scale = 0.8
for i in range(originalDoc.Pages.Count):
    page = originalDoc.Pages.get_Item(i)
    # Use same scale to set width and height
    width = page.Size.Width * scale
    height = page.Size.Height * scale
    # Add new page with expected width and height
    newPage = newDoc.Pages.Add(SizeF(width, height), margins)
    newPage.Canvas.ScaleTransform(scale, scale)
    # Copy content of original page into new page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF.Empty())
```

---

# spire.pdf page rotation
## rotate an existing PDF page
```python
# Get the first page of the loaded PDF file
page = doc.Pages[0]
# Get the original rotation angle
rotation = int(page.Rotation.value)
# Set the angle
rotation += int(PdfPageRotateAngle.RotateAngle270.value)
# Rotate the PDF page based on
page.Rotation = PdfPageRotateAngle(rotation)
```

---

# Spire.PDF Page Rotation
## Create a PDF document with rotated page
```python
# Create a pdf document
doc = PdfDocument()
# Create PdfUnitConvertor to convert the unit
unitCvtr = PdfUnitConvertor()
# Setting for page margin
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    2.0, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
# Create PdfSection
section = doc.Sections.Add()
# Set "A4" for Pdf page
section.PageSettings.Size = PdfPageSize.A4()
# Set page margin
section.PageSettings.Margins = margin
# Set rotating angle
section.PageSettings.Rotate = PdfPageRotateAngle.RotateAngle90
# Add the page
page = section.Pages.Add()
# Define a PdfBrush
brush = PdfBrushes.get_Black()
# Define a font
font = PdfTrueTypeFont("Arial", 13.0, PdfFontStyle.Bold, True)
# Set the string format
format = PdfStringFormat(PdfTextAlignment.Left)
# Set the position for drawing
x = 0.0
y = 50.0
# Text string
specification = "The sample demonstrates how to rotate page when creating a PDF document."
# Draw text string on page canvas
page.Canvas.DrawString(specification, font, brush, x, y, format)
```

---

# Spire.PDF Page Orientation Setting
## Set PDF page orientation based on image dimensions
```python
#Create a pdf document
doc = PdfDocument()
#Add a section
section = doc.Sections.Add()
#Check whether the width of the image file is greater than default page width or not
if image.PhysicalDimension.Width > section.PageSettings.Size.Width:
    #Set the orientation as landscape
    section.PageSettings.Orientation = PdfPageOrientation.Landscape
else:
    section.PageSettings.Orientation = PdfPageOrientation.Portrait
#Add a new page with orientation
page = section.Pages.Add()
```

---

# Spire.PDF Tab Order Setting
## Set tab order for PDF document
```python
#Set using document structure
pdf.FileInfo.IncrementalUpdate = False
page = pdf.Pages[0]
page.SetTabOrder(TabOrder.Structure)
```

---

# spire.pdf page splitting
## Split a PDF page into multiple pages
```python
#Get the first page
page = doc.Pages[0]
#Create a new Pdf
newPdf = PdfDocument()
#Remove all the margins
newPdf.PageSettings.Margins.All = 0.0
#Set the page size of new Pdf
newPdf.PageSettings.Width = page.Size.Width
newPdf.PageSettings.Height = page.Size.Height / float(2)
#Add a new page
newPage = newPdf.Pages.Add()
format = PdfTextLayout()
format.Break = PdfLayoutBreakType.FitPage
format.Layout = PdfLayoutType.Paginate
#Draw the page in the new page
page.CreateTemplate().Draw(newPage, PointF(0.0, 0.0), format)
```

---

# Spire.PDF Page Splitting
## Split a PDF file by extracting particular pages
```python
# Create a new PDF document
newPdf = PdfDocument()
# Initialize a new instance of PdfPageBase class
page = None
# Specify the pages which you want them to be split
for i in range(1, 3):
    # Add same size page for newPdf
    page = newPdf.Pages.Add(oldPdf.Pages[i].Size, PdfMargins(0.0))
    # Create template of the oldPdf page and draw into newPdf page
    oldPdf.Pages[i].CreateTemplate().Draw(page, PointF(0.0, 0.0))
```

---

# PDF Page Content Zooming
## Zoom PDF page contents to fit a new page size
```python
#Create a new document
newDoc = PdfDocument()
#Iterate through pages of the source document
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    #Add new page with 'A3' size
    newPage = newDoc.Pages.Add(PdfPageSize.A3(), PdfMargins(0.0,0.0))
    #Zoom content to the new page
    newPage.Canvas.ScaleTransform(newPage.ActualSize.Width / float(page.ActualSize.Width), (newPage.ActualSize.Height / float(page.ActualSize.Height)))
    #Draw the page to new page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(0.0, 0.0))
```

---

# Spire.PDF Python Layers
## Add layers to PDF document
```python
page = doc.Pages[0]
#create a layer named "red line"
layer = doc.Layers.AddLayer("red line",PdfVisibility.On)
pcA = layer.CreateGraphics(page.Canvas)
pcA.DrawLine(PdfPen(PdfBrushes.get_Red(), 2.0), PointF(100.0, 350.0), PointF(300.0, 350.0))
#create a layer named "blue line"
layer = doc.Layers.AddLayer("blue line")
pcB = layer.CreateGraphics(doc.Pages[0].Canvas)
pcB.DrawLine(PdfPen(PdfBrushes.get_Blue(), 2.0), PointF(100.0, 400.0), PointF(300.0, 400.0))
#create a layer named "green line"
layer = doc.Layers.AddLayer("green line")
pcC = layer.CreateGraphics(doc.Pages[0].Canvas)
pcC.DrawLine(PdfPen(PdfBrushes.get_Green(), 2.0), PointF(100.0, 450.0), PointF(300.0, 450.0))
```

---

# Spire.PDF Booklet Creation
## Create a booklet from a PDF document with specified dimensions
```python
#Create a pdf document
doc = PdfDocument()
width = PdfPageSize.A4().Width * 2
height = PdfPageSize.A4().Height
doc.CreateBooklet(inputFile, width, height, True)
```

---

# Spire.PDF Change PDF Version
## Change the version of a PDF document
```python
# Create PDF document
doc = PdfDocument()
# Change the PDF version
doc.FileInfo.Version = PdfVersion.Version1_6
```

---

# Spire.PDF Document Comparison
## Compare two PDF documents and save the comparison result
```python
#Load the pdf document
doc1 = PdfDocument()
doc1.LoadFromFile(inputFile1)

doc2 = PdfDocument()
doc2.LoadFromFile(inputFile2)

# Create a PDF comparer object
compare = PdfComparer(doc1, doc2)

# Save the result of the comparison to a new PDF document
compare.Compare(outputFile)
```

---

# PDF Document Compression
## Compress PDF document by setting compression level and compressing images
```python
# Compress the content in document
doc.FileInfo.IncrementalUpdate = False
# Set the compression level to best
doc.CompressionLevel = PdfCompressionLevel.Best
# Disable the incremental update
doc.FileInfo.IncrementalUpdate = False
# Traverse all pages
imageHelper = PdfImageHelper()
for i in range(doc.Pages.Count):
    page = doc.Pages[i]
    if page is not None:
        imagesInfo = imageHelper.GetImagesInfo(page)
        if (len(imagesInfo) > 0):
            for j in range(len(imagesInfo)):
                imagesInfo[j].TryCompressImage()
```

---

# Creating a Multilayer PDF Document
## This code demonstrates how to create a PDF document with multiple layers (text and image)
```python
doc = PdfDocument()
# Creates a page
page = doc.Pages.Add()
# Create text
text = "Welcome to evaluate Spire.PDF for Python !"
format = PdfStringFormat(PdfTextAlignment.Left)
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
# Defines a font
font = PdfTrueTypeFont("Calibri", 15.0, PdfFontStyle.Regular, True)
x = 50.0
y = 50.0
# Draw text layer
page.Canvas.DrawString(text, font, brush, PointF(x, y), format)
size = font.MeasureString("Welcome to  evaluate", format)
size2 = font.MeasureString("Spire.PDF for Python", format)
# Loads an image 
image = PdfImage.FromFile("./Demos/Data/MultilayerImage.png")
# Draw image layer
page.Canvas.DrawImage(image, PointF(x + size.Width, y), size2)
# Save the document
doc.SaveToFile("CreateMultilayerPDF.pdf")
doc.Close()
```

---

# Spire.PDF PDF/A-1B Creation
## Create a PDF document and convert it to PDF/A-1B standard
```python
doc = PdfNewDocument()
# Create one A4 page
page = doc.Pages.Add(PdfPageSize.A4(), PdfMargins(40.0))
# Draw content
pageWidth = page.Canvas.ClientSize.Width
y = 0.0
# Title
y = y + 5
brush = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
titleFont = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
titleFormat = PdfStringFormat(PdfTextAlignment.Center)
titleFormat.CharacterSpacing = 1
titleText = "Summary of Science"
page.Canvas.DrawString(titleText, titleFont, brush, pageWidth / 2, y, titleFormat)
size = titleFont.MeasureString(titleText, titleFormat)
y = y + size.Height + 6
# Reference content
refFont = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Regular, True)
refFormat = PdfStringFormat()
refFormat.ParagraphIndent = refFont.Size * 2
refFormat.MeasureTrailingSpaces = True
refFormat.LineSpacing = refFont.Size * 1.5
refText1 = "(All text and picture from "
refText2 = "Wikipedia"
refText3 = ", the free encyclopedia)"
page.Canvas.DrawString(refText1, refFont, brush, 0.0, y, refFormat)
size = refFont.MeasureString(refText1, refFormat)
x1 = size.Width
refFormat.ParagraphIndent = 0.0
linkFont = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Underline, True)
linkBrush = PdfBrushes.get_Blue()
page.Canvas.DrawString(refText2, linkFont, linkBrush, x1, y, refFormat)
size = linkFont.MeasureString(refText2, refFormat)
x1 = x1 + size.Width
page.Canvas.DrawString(refText3, refFont, brush, x1, y, refFormat)
y = y + size.Height
# Content
contentFormat = PdfStringFormat()
contentFont = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
contentFormat.LineSpacing = contentFont.Size * 1.5
textWidget = PdfTextWidget("Sample text content", contentFont, brush)
textLayout = PdfTextLayout()
textLayout.Break = PdfLayoutBreakType.FitPage
textLayout.Layout = PdfLayoutType.Paginate
bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
textWidget.StringFormat = contentFormat
textWidget.Draw(page, bounds, textLayout)
# Save the document
stream = Stream("output.pdf")
doc.Save(stream)
converter = PdfStandardsConverter(stream)
converter.ToPdfA1B("output_a1b.pdf")
doc.Close()
```

---

# Create PDF Portfolio
## This code demonstrates how to create a PDF portfolio by adding files and creating subfolders
```python
# Create PDF document
doc = PdfDocument()
# Loop through files and add them to the portfolio
i = 0
while i < num_files:
    # Add file to the collection
    doc.Collection.Folders.AddFile(file_path)
    # Create subfolder and add file to it
    folder = doc.Collection.Folders.CreateSubfolder("SubFolder" + str(i + 1))
    folder.AddFile(file_path)
    i += 1
```

---

# Spire.PDF Two Column Creation
## Create a PDF document with two columns of text
```python
# Creates a pdf document
doc = PdfDocument()
# Creates a new page
page = doc.Pages.Add()
s1 = "Spire.PDF for .NET is a professional PDF component applied to creating, writing, " + "editing, handling and reading PDF files without any external dependencies within " + ".NET application. Using this .NET PDF library, you can implement rich capabilities " + "to create PDF files from scratch or process existing PDF documents entirely through " + "C#/VB.NET without installing Adobe Acrobat."
s2 = "Many rich features can be supported by the .NET PDF API, such as security setting " + "(including digital signature), PDF text/attachment/image extract, PDF merge/split " + ", metadata update, section, graph/image drawing and inserting, table creation and " + "processing, and importing data etc.Besides, Spire.PDF for .NET can be applied to easily " + "converting Text, Image and HTML to PDF with C#/VB.NET in high quality."
# Get width and height of page
pageWidth = page.GetClientSize().Width
pageHeight = page.GetClientSize().Height
brush = PdfBrushes.get_Black()
font = PdfFont(PdfFontFamily.TimesRoman, 12.0)
format = PdfStringFormat(PdfTextAlignment.Justify)
# Draw text
page.Canvas.DrawString(s1, font, brush, RectangleF(0.0, 20.0, pageWidth / 2 - 8, pageHeight), format)
page.Canvas.DrawString(s2, font, brush, RectangleF(pageWidth / 2 + 8, 20.0, pageWidth / 2 - 8, pageHeight), format)
```

---

# Spire.PDF Custom Document Properties
## Set custom properties for PDF document
```python
# Custom document properties
doc.DocumentInformation.SetCustomProperty("Company", "E-iceblue")
doc.DocumentInformation.SetCustomProperty("Component", "Spire.PDF for .NET")
doc.DocumentInformation.SetCustomProperty("Name", "Daisy")
doc.DocumentInformation.SetCustomProperty("Team", "SalesTeam")
```

---

# Spire.PDF Delete Layer
## Remove a specific layer from PDF document
```python
# Delete the "red line" layer from PDF document
doc.Layers.RemoveLayer("red line")
```

---

# PDF Document Properties Extraction
## Extract PDF document metadata properties

```python
# Create a PDF document object
doc = PdfDocument()

# Load the PDF file
doc.LoadFromFile(inputFile)

# Get document information
docInfo = doc.DocumentInformation

# Extract document properties
author = docInfo.Author
creationDate = docInfo.CreationDate.ToString()
keywords = docInfo.Keywords
modifyDate = docInfo.ModificationDate.ToString()
subject = docInfo.Subject
title = docInfo.Title
```

---

# Spire.PDF Viewer Preferences
## Get PDF document viewer preferences
```python
viewer = doc.ViewerPreferences
# Create a list to store the preference details
builder = []
builder.append("Whether the documents window position is in the center: ")
builder.append("CenterWindow: " + str(viewer.CenterWindow))
builder.append("Document displaying mode, i.e. show thumbnails, full-screen, show attachment panel: ")
builder.append("PageMode: " + str(viewer.PageMode))
builder.append("The page layout, i.e. single page, one column: ")
builder.append("PageLayout: " + str(viewer.PageLayout))
builder.append("Whether window's title bar should display document title: ")
builder.append("DisplayTitle: " + str(viewer.DisplayTitle))
builder.append("Whether to resize the document's window to fit the size of the firstdisplayed page: ")
builder.append("FitWindow:" + str(viewer.FitWindow))
builder.append("Whether to hide menu bar of the viewer application: ")
builder.append("HideMenubar: " + str(viewer.HideMenubar))
builder.append("Whether to hide tool bar of the viewer application: ")
builder.append("HideToolbar: " + str(viewer.HideToolbar))
builder.append("Whether to hide UI elements like scroll bars and leave only the page contents displayed: ")
builder.append("HideWindowUI: " + str(viewer.HideWindowUI))
```

---

# Spire.PDF Get Zoom Factor
## Extract the zoom factor from a PDF document
```python
# Create a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
action = doc.AfterOpenAction
zoomvalue = action.Destination.Zoom
result = "The zoom factor of the document is "+ str(zoomvalue*100) +"%."
```

---

# Spire.PDF Python Invisible Layers
## Code to make all PDF layers invisible
```python
#Create a new PDF document.
doc = PdfDocument()
for i in range(doc.Layers.Count):
    #Set all the Pdf layers invisible.
    doc.Layers.get_Item(i).Visibility = PdfVisibility.Off
doc.Close()
```

---

# Spire.PDF Python Layers
## Set particular PDF layers to be invisible
```python
#Create a new PDF document.
doc = PdfDocument()
#Set the first layer invisible.
doc.Layers.get_Item(0).Visibility = PdfVisibility.Off
#Set the layer named "blue line" invisible.
doc.Layers.get_Item("blue line").Visibility = PdfVisibility.Off
```

---

# Spire.PDF Portfolio Check
## Check if a PDF document is a portfolio
```python
# Create a pdf document
doc = PdfDocument()
# Load from file
doc.LoadFromFile(inputFile)
# Judge whether the document is portfolio or not
value = doc.IsPortfolio
if value:
    builder = "The document is portfolio"
else:
    builder = "The document is not portfolio"
```

---

# Spire.PDF document merging
## Merge multiple PDF documents by appending and importing pages
```python
# Create PDF document list
docs = [None for _ in range(len(files))]
i = 0
while i < len(files):
    docs[i] = PdfDocument()
    docs[i].LoadFromFile(files[i])
    i += 1

# Append document
docs[0].AppendPage(docs[1])

# Import pages
for i in range(0, docs[2].Pages.Count, 2):
    docs[0].InsertPage(docs[2], i)
```

---

# Spire.PDF Python Merge PDFs by Stream
## Merge multiple PDF documents using streams
```python
# Create PDF document streams 
stream1 = Stream(inputFile1)
stream2 = Stream(inputFile2)
stream3 = Stream(inputFile3)
# PDF document streams collection
streams = [stream1, stream2, stream3]
mergeOp = MergerOptions()
PdfMerger.MergeByStream(streams, outputFile, mergeOp)
```

---

# Spire.PDF Page Margin Modification
## Modify PDF document page margins by creating a new document with adjusted margins
```python
# Creates a new pdf document
newDoc = PdfDocument()
# Defines the page margins of the new document
top = 50.0
bottom = 50.0
left = 50.0
right = 50.0
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Adds a new page to the new document and set the page size to be the same as the source document
    newPage = newDoc.Pages.Add(page.Size, PdfMargins(0.0))
    # Set the scale of the new document content
    newPage.Canvas.ScaleTransform((page.ActualSize.Width - left - right) / page.ActualSize.Width, (page.ActualSize.Height - top - bottom) / page.ActualSize.Height)
    # Draws the content of the source page onto the new document page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(left, top))
```

---

# PDF Document Properties Management
## Set PDF document information and file properties
```python
#Load pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
#Set document info
doc.DocumentInformation.Author = "E-iceblue"
doc.DocumentInformation.Creator = "E-iceblue"
doc.DocumentInformation.Keywords = "pdf, demo, document information"
doc.DocumentInformation.Producer = "Spire.Pdf"
doc.DocumentInformation.Subject = "Demo of Spire.Pdf"
doc.DocumentInformation.Title = "Document Information"
#File info
doc.FileInfo.CrossReferenceType = PdfCrossReferenceType.CrossReferenceStream
doc.FileInfo.IncrementalUpdate = False
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()
```

---

# Spire.PDF Page Rearrangement
## Rearrange the order of pages in a PDF document
```python
#Create a pdf document
doc = PdfDocument()
#Rearrange the page order
doc.Pages.ReArrange([1, 0])
```

---

# spire.pdf page margin removal
## remove margins from pdf pages
```python
# Creates a new document
newDoc = PdfDocument()
# Get page margins of source pdf page
margins = doc.PageSettings.Margins
top = margins.Left
bottom = margins.Bottom
left = margins.Left
right = margins.Right
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)
    # Adds a new page to the new document
    newPage = newDoc.Pages.Add(SizeF(page.Size.Width - left - right, page.Size.Height - top - bottom), PdfMargins(0.0))
    # Draws the content of the source page onto the new document page
    newPage.Canvas.DrawTemplate(page.CreateTemplate(), PointF(-left, -top))
```

---

# spire.pdf python set expiry date
## Set an expiry date for PDF document using JavaScript action
```python
# Create JavaScript to check expiry date
javaScript = "var rightNow = new Date();" + "var endDate = new Date('October 20, 2015 23:59:59');" + "if(rightNow.getTime() > endDate)" + "app.alert('This document has expired, please contact us for a new one.',1);" + "this.closeDoc();"
js = PdfJavaScriptAction(javaScript)
doc.AfterOpenAction = js
```

---

# Spire.PDF Python Set Zoom Factor
## Set zoom factor for PDF document when opened
```python
#Get the first page
page = doc.Pages[0]
#Set pdf destination
dest = PdfDestination(page)
dest.Mode = PdfDestinationMode.Location
dest.Location = PointF(-40.0, -40.0)
dest.Zoom = 0.6
#Set action
gotoAction = PdfGoToAction(dest)
doc.AfterOpenAction = gotoAction
```

---

# Spire.PDF Document Splitting
## Split a PDF document into multiple files
```python
#Open pdf document
doc = PdfDocument()
doc.LoadFromFile("input.pdf")  # Replace with actual input file path
pattern = "SplitDocument-{0}.pdf"
#Split document
doc.Split(pattern)
lastPageFileName = ("SplitDocument-{0:d}.pdf").format(doc.Pages.Count - 1)
doc.Close()
```

---

# Spire.PDF Template Creation
## Create PDF document with templates, sections and pages
```python
def DrawPage( page):
    pageWidth = page.Canvas.ClientSize.Width
    y = 0.0
    # Title
    y = y + 5
    brush2 = PdfSolidBrush(PdfRGBColor(Color.get_Black()))
    font2 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold, True)
    format2 = PdfStringFormat(PdfTextAlignment.Center)
    format2.CharacterSpacing = 1.0
    text = "Summary of Science"
    page.Canvas.DrawString(text, font2, brush2, pageWidth / 2, y, format2)
    size = font2.MeasureString(text, format2)
    y = y + size.Height + 6
    # Icon
    image = PdfImage.FromFile(inputFile3)
    page.Canvas.DrawImage(image, PointF(
        pageWidth - image.PhysicalDimension.Width, y))
    imageLeftSpace = pageWidth - image.PhysicalDimension.Width - 2
    imageBottom = image.PhysicalDimension.Height + y
    # Reference content
    font3 = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Regular, True)
    format3 = PdfStringFormat()
    format3.ParagraphIndent = font3.Size * 2
    format3.MeasureTrailingSpaces = True
    format3.LineSpacing = font3.Size * 1.5
    text1 = "(All text and picture from "
    text2 = "Wikipedia"
    text3 = ", the free encyclopedia)"
    page.Canvas.DrawString(text1, font3, brush2, 0.0, y, format3)
    size = font3.MeasureString(text1, format3)
    x1 = size.Width
    format3.ParagraphIndent = 0
    font4 = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Underline, True)
    brush3 = PdfBrushes.get_Blue()
    page.Canvas.DrawString(text2, font4, brush3, x1, y, format3)
    size = font4.MeasureString(text2, format3)
    x1 = x1 + size.Width
    page.Canvas.DrawString(text3, font3, brush2, x1, y, format3)
    y = y + size.Height
    # Content
    format4 = PdfStringFormat()
    font5 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular, True)
    format4.LineSpacing = font5.Size * 1.5
    textLayouter = PdfStringLayouter()
    imageLeftBlockHeight = imageBottom - y
    result = textLayouter.Layout(text, font5, format4, SizeF(
        imageLeftSpace, imageLeftBlockHeight))
    if result.ActualSize.Height < imageBottom - y:
        imageLeftBlockHeight = imageLeftBlockHeight + result.LineHeight
        result = textLayouter.Layout(text, font5, format4, SizeF(
            imageLeftSpace, imageLeftBlockHeight))
    for line in result.Lines:
        page.Canvas.DrawString(line.Text, font5, brush2, 0.0, y, format4)
        y = y + result.LineHeight
    textWidget = PdfTextWidget(result.Remainder, font5, brush2)
    textLayout = PdfTextLayout()
    textLayout.Break = PdfLayoutBreakType.FitPage
    textLayout.Layout = PdfLayoutType.Paginate
    bounds = RectangleF(PointF(0.0, y), page.Canvas.ClientSize)
    textWidget.StringFormat = format4
    newPage = PdfNewPage(page)
    textWidget.Draw(newPage, bounds, textLayout)

def SetDocumentTemplate( doc, pageSize, margin):
    leftSpace = PdfPageTemplateElement(margin.Left, pageSize.Height)
    doc.Template.Left = leftSpace
    topSpace = PdfPageTemplateElement(pageSize.Width, margin.Top)
    topSpace.Foreground = True
    doc.Template.Top = topSpace
    # Draw header label
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(PdfTextAlignment.Right)
    label = "Demo of Spire.Pdf"
    size = font.MeasureString(label, format)
    y = topSpace.Height - font.Height - 1
    pen = PdfPen(PdfRGBColor(Color.get_Black()), 0.75)
    topSpace.Graphics.SetTransparency(0.5)
    topSpace.Graphics.DrawLine(
        pen, margin.Left, y, pageSize.Width - margin.Right, y)
    y = y - 1 - size.Height
    topSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_Black(), pageSize.Width - margin.Right, y, format)
    rightSpace = PdfPageTemplateElement(margin.Right, pageSize.Height)
    doc.Template.Right = rightSpace
    bottomSpace = PdfPageTemplateElement(pageSize.Width, margin.Bottom)
    bottomSpace.Foreground = True
    doc.Template.Bottom = bottomSpace
    # Draw footer label
    y = font.Height + 1
    bottomSpace.Graphics.SetTransparency(0.5)
    bottomSpace.Graphics.DrawLine(
        pen, margin.Left, y, pageSize.Width - margin.Right, y)
    y = y + 1
    pageNumber = PdfPageNumberField()
    pageCount = PdfPageCountField()
    pageNumberLabel = PdfCompositeField()
    pageNumberLabel.AutomaticFields = [pageNumber, pageCount]
    pageNumberLabel.Brush = PdfBrushes.get_Black()
    pageNumberLabel.Font = font
    pageNumberLabel.StringFormat = format
    pageNumberLabel.Text = "page {0} of {1}"
    pageNumberLabel.Draw(bottomSpace.Graphics,
                         pageSize.Width - margin.Right, y)
    headerImage = PdfImage.FromFile(inputFile1)
    pageLeftTop = PointF(-margin.Left, -margin.Top)
    header = PdfPageTemplateElement(
        pageLeftTop, headerImage.PhysicalDimension)
    header.Foreground = False
    header.Graphics.SetTransparency(0.5)
    header.Graphics.DrawImage(headerImage, 0.0, 0.0)
    doc.Template.Stamps.Add(header)
    footerImage = PdfImage.FromFile(inputFile2)
    y = pageSize.Height - footerImage.PhysicalDimension.Height
    footerLocation = PointF(-margin.Left, y)
    footer = PdfPageTemplateElement(
        footerLocation, footerImage.PhysicalDimension)
    footer.Foreground = False
    footer.Graphics.SetTransparency(0.5)
    footer.Graphics.DrawImage(footerImage, 0.0, 0.0)
    doc.Template.Stamps.Add(footer)

def SetSectionTemplate( section, pageSize, margin, label):
    leftSpace = PdfPageTemplateElement(margin.Left, pageSize.Height)
    leftSpace.Foreground = True
    section.Template.OddLeft = leftSpace
    font = PdfTrueTypeFont("Arial", 9.0, PdfFontStyle.Italic, True)
    format = PdfStringFormat(
        PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
    y = (pageSize.Height - margin.Top - margin.Bottom) * (1 - 0.618)
    bounds = RectangleF(10.0, y, margin.Left - 20, font.Height + 6)
    leftSpace.Graphics.DrawRectangle(PdfBrushes.get_OrangeRed(), bounds)
    leftSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_White(), bounds, format)
    rightSpace = PdfPageTemplateElement(margin.Right, pageSize.Height)
    rightSpace.Foreground = True
    section.Template.EvenRight = rightSpace
    bounds = RectangleF(10.0, y, margin.Right - 20, font.Height + 6)
    rightSpace.Graphics.DrawRectangle(PdfBrushes.get_SaddleBrown(), bounds)
    rightSpace.Graphics.DrawString(
        label, font, PdfBrushes.get_White(), bounds, format)

# Create a pdf document
doc = PdfDocument()
doc.ViewerPreferences.PageLayout = PdfPageLayout.TwoColumnLeft
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left
SetDocumentTemplate(doc, PdfPageSize.A4(), margin)
# Create one section
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = PdfMargins(0.0)
SetSectionTemplate(section, PdfPageSize.A4(), margin, "Section 1")
# Create one page
page = section.Pages.Add()
# Draw page
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
page = section.Pages.Add()
DrawPage(page)
```

---

# Spire.PDF Page Transitions
## Demonstrate how to create a PDF document with different page transition effects
```python
# Create a pdf document
doc = PdfDocument()
doc.ViewerPreferences.PageMode = PdfPageMode.FullScreen
# Set the margin
unitCvtr = PdfUnitConvertor()
margin = PdfMargins()
margin.Top = unitCvtr.ConvertUnits(
    2.54, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Bottom = margin.Top
margin.Left = unitCvtr.ConvertUnits(
    3.17, PdfGraphicsUnit.Centimeter, PdfGraphicsUnit.Point)
margin.Right = margin.Left

# Create section with Fly transition
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Fly
section.PageSettings.Transition.PageDuration = 1.0

# Create section with Box transition
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Box
section.PageSettings.Transition.PageDuration = 1.0

# Create section with Split transition
section = doc.Sections.Add()
section.PageSettings.Size = PdfPageSize.A4()
section.PageSettings.Margins = margin
section.PageSettings.Transition.Duration = 2.0
section.PageSettings.Transition.Style = PdfTransitionStyle.Split
section.PageSettings.Transition.Dimension = PdfTransitionDimension.Vertical
section.PageSettings.Transition.Motion = PdfTransitionMotion.Inward
section.PageSettings.Transition.PageDuration = 1.0
```

---

# PDF Viewer Preferences
## Set viewer preferences for a PDF document including window centering, title display, window fitting, and UI element visibility
```python
#Set view reference
doc.ViewerPreferences.CenterWindow = True
doc.ViewerPreferences.DisplayTitle = False
doc.ViewerPreferences.FitWindow = False
doc.ViewerPreferences.HideMenubar = True
doc.ViewerPreferences.HideToolbar = True
doc.ViewerPreferences.PageLayout = PdfPageLayout.SinglePage
```

---

