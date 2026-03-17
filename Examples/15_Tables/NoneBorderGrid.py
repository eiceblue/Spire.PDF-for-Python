from spire.pdf import *
from spire.pdf.common import *

# Create a new PDF document
doc = PdfDocument()

# Add a page to the document
page = doc.Pages.Add()

# Create a new grid
grid = PdfGrid()

# Add a row to the grid
row1 = grid.Rows.Add()

# Add 2 columns to the grid
grid.Columns.Add(2)

# Set border dash style for specific cell in the row
row1.Cells.get_Item(0).Style.Borders.Bottom.DashStyle = PdfDashStyle.none
row1.Cells.get_Item(0).Style.Borders.Top.DashStyle = PdfDashStyle.none
row1.Cells.get_Item(0).Style.Borders.Right.DashStyle = PdfDashStyle.none
row1.Cells.get_Item(0).Style.Borders.Left.DashStyle = PdfDashStyle.none

# Set cell values in the row
str = "Hello Word!"
for i in range(grid.Columns.Count):
    row1.Cells[i].Value = str

# Draw the grid on the page at the specified position
grid.Draw(page, PointF(0.0, 50.0))

# Save the document as a PDF file with no borders in the grid
result = "PDFNoneBorderGrid.pdf"
doc.SaveToFile(result, FileFormat.PDF)

doc.Dispose()