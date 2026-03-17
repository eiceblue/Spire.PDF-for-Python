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
row0 = grid.Rows.Add()
row1 = grid.Rows.Add()

height = 21.0

#Iterate each row of grid
for i in range(grid.Rows.Count) :
    #Set the height for row 
    grid.Rows[i].Height = height

# Draw the grid on the page at the specified location
grid.Draw(page, PointF(10.0, 100.0))

# Set font styles for specific rows and cells
trueTypeFont1 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Bold,True)
trueTypeFont2 = PdfTrueTypeFont("Arial", 16.0, PdfFontStyle.Italic,True)
row0.Style.Font =  trueTypeFont1
row1.Style.Font = trueTypeFont2

row0.Cells[0].Value = "Corporation"

# Merge two rows
row0.Cells[0].RowSpan = 2

row0.Cells[1].Value = "B&K Undersea Photo"
row0.Cells[1].StringFormat = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

# Merge two columns
row0.Cells[1].ColumnSpan = 3

# Set value for cell and set style for it
row0.Cells[4].Value = "World"
trueTypeFont3 = PdfTrueTypeFont("Arial", 10.0, PdfFontStyle.Bold,True)
row0.Cells[4].Style.Font = trueTypeFont3
row0.Cells[4].StringFormat = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)
row0.Cells[4].Style.BackgroundBrush = PdfBrushes.get_LightGreen()

row1.Cells[1].Value = "Diving International Unlimited"
row1.Cells[1].StringFormat = PdfStringFormat(PdfTextAlignment.Center, PdfVerticalAlignment.Middle)

# Merge four columns
row1.Cells[1].ColumnSpan = 4

# Draw the updated grid on the page at a different location
grid.Draw(page, PointF(10.0, 300.0))

# Save the pdf document with merged cells to a file
doc.SaveToFile("MergeCells.pdf")

doc.Dispose()