from spire.pdf import *
from spire.pdf.common import *

# Create a new PDF document instance
pdf = PdfDocument()

# Load an existing PDF file from the specified path
pdf.LoadFromFile("Data/Sample.pdf")

# Get the first page (index 0) of the loaded PDF document
page = pdf.Pages[0]

# Initialize a text finder object for the selected page
finder = PdfTextFinder(page)

# Set the text search option to match whole words only
finder.Options.Parameter = TextFindParameter.WholeWord

# Update the text search option to also ignore case during matching
finder.Options.Parameter = TextFindParameter.IgnoreCase

# Search for the specified text string on the page and get all matching fragments
fragments = finder.Find("An older meaning still in use today is that of Aristotle, for whom scientific knowledge was a body of reliable knowledge that can be logically and rationally explained.")

# Retrieve the first matched text fragment
textFragment = fragments[0]

# Define the annotation note text to be added
text = "There is a markup annotation added by Spire.PDF for Python."

# Initialize a list to store quadrilateral points for each character or word bounding box;
# each rectangle requires 4 points, so total size is 4 times the number of bounds
quadPoints = [None for _ in range(len(textFragment.Bounds) * 4)]

# Iterate over each bounding rectangle of the found text fragment
for i in range(len(textFragment.Bounds)):
    # Get the current bounding rectangle
    rect = textFragment.Bounds[i]
    
    # Assign the top-left corner of the rectangle as the first quad point
    quadPoints[4 * i] = PointF(rect.Left, rect.Top)
    
    # Assign the top-right corner of the rectangle as the second quad point
    quadPoints[4 * i + 1] = PointF(rect.Right, rect.Top)
    
    # Assign the bottom-left corner of the rectangle as the third quad point
    quadPoints[4 * i + 2] = PointF(rect.Left, rect.Bottom)
    
    # Assign the bottom-right corner of the rectangle as the fourth quad point
    quadPoints[4 * i + 3] = PointF(rect.Right, rect.Bottom)

# Create a text markup annotation using the first bounding rectangle and the computed quad points
annotation = PdfTextMarkupAnnotation(textFragment.Bounds[0], quadPoints)

# Set the popup note text for the annotation
annotation.Text = text

# Set the highlight color of the markup annotation to blue
annotation.TextMarkupColor = PdfRGBColor(Color.get_Blue())

# Add the created annotation to the page's annotation collection
page.Annotations.Add(annotation)

# Save the modified PDF document to a new file
pdf.SaveToFile("AddAnnotationsToMulti-lineText.pdf")

# Close the PDF document and release resources
pdf.Close()