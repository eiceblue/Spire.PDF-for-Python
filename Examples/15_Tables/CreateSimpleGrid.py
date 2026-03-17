from spire.pdf import *
from spire.pdf.common import *

#Create a pdf document 
doc = PdfDocument()

#Add a new page
page = doc.Pages.Add()

#Create a grid
grid = PdfGrid()
grid.Columns.Add(5)

#Iterate each column of grid
for j in range(grid.Columns.Count):
    #Set width of column
    grid.Columns[j].Width = 100

#Add rows
for i in range(10):
    grid.Rows.Add()

# Set font styles for specific rows and cells
trueTypeFont = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Regular,True)

height = 21.0

#Iterate each row of grid
for i in range(grid.Rows.Count):
    gridRow = grid.Rows.get_Item(i)
    #Set the height for row 
    gridRow.Height = height
    gridRow.Style.Font =  trueTypeFont

    for j in range(gridRow.Cells.Count):
        gridRow.Cells.get_Item(j).Value = "Row_"+ str(i+1) + "Cell_"+ str(j+1) 
        gridRow.Cells.get_Item(j).StringFormat = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

# Draw the updated grid on the page at a different location
grid.Draw(page, PointF(10.0, 100.0))

# Save the pdf document to a file
doc.SaveToFile("SimpleGrid.pdf")

doc.Dispose()