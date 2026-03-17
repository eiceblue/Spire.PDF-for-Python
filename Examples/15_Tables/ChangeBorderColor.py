from spire.pdf import *
from spire.pdf.common import *

#Create a pdf document
document =  PdfDocument()

#Add a new page
page = document.Pages.Add()

data = [
         "VendorName;Address1;City;State;Country",
         "Cacor Corporation;161 Southfield Rd;Southfield;OH;U.S.A.",
         "Underwater;50 N 3rd Street;Indianapolis;IN;U.S.A.",
         "J.W.  Luscher Mfg.;65 Addams Street;Berkely;MA;U.S.A.",
         "Scuba Professionals;3105 East Brace;Rancho Dominguez;CA;U.S.A.",
         "Divers'  Supply Shop;5208 University Dr;Macon;GA;U.S.A.",
         "Techniques;52 Dolphin Drive;Redwood City;CA;U.S.A.",
         "Perry Scuba;3443 James Ave;Hapeville;GA;U.S.A.",
         "Beauchat, Inc.;45900 SW 2nd Ave;Ft Lauderdale;FL;U.S.A.",
         "Amor Aqua;42 West 29th Street;New York;NY;U.S.A.",
         "Aqua Research Corp.;P.O. Box 998;Cornish;NH;U.S.A.",
         "B&K Undersea Photo;116 W 7th Street;New York;NY;U.S.A.",
         "Diving International Unlimited;1148 David Drive;San Diego;DA;U.S.A.",
         "Nautical Compressors;65 NW 167 Street;Miami;FL;U.S.A.",
         "Glen Specialties, Inc.;17663 Campbell Lane;Huntington Beach;CA;U.S.A.",
         "Dive Time;20 Miramar Ave;Long Beach;CA;U.S.A.",
         "Undersea Systems, Inc.;18112 Gotham Street;Huntington Beach;CA;U.S.A.",
         "Felix Diving;310 S Michigan Ave;Chicago;IL;U.S.A.",
         "Central Valley Skin Divers;160 Jameston Ave;Jamaica;NY;U.S.A.",
         "Parkway Dive Shop;241 Kelly Street;South Amboy;NJ;U.S.A.",
         "Marine Camera & Dive;117 South Valley Rd;San Diego;CA;U.S.A.",
         "Dive Canada;275 W Ninth Ave;Vancouver;British Columbia;Canada",
         "Dive & Surf;P.O. Box 20210;Indianapolis;IN;U.S.A.",
         "Fish Research Labs;29 Wilkins Rd Dept. SD;Los Banos;CA;U.S.A."
]
      
#Create a grid
grid = PdfGrid()

#Add rows
for r in range(len(data)):
   row = grid.Rows.Add()

#Add columns
grid.Columns.Add(5)

#Set the width for column
grid.Columns[0].Width = 120
grid.Columns[1].Width = 120
grid.Columns[2].Width = 120
grid.Columns[3].Width = 50
grid.Columns[4].Width = 60

#set the height of rows
height = page.Canvas.ClientSize.Height - (grid.Rows.Count + 1)
for i in range(grid.Rows.Count):
    grid.Rows[i].Height = 12.5

for r in range(len(data)):
    #Insert data to grid
    rowData = data[r].split(';')
    for c in range(len(rowData)):
        grid.Rows[r].Cells[c].Value = rowData[c]        

#Set the font 
trueTypeFont = PdfTrueTypeFont("Arial", 8.0, PdfFontStyle.Bold,True)
grid.Rows[0].Style.Font = trueTypeFont

 #Set color of border
border = PdfBorders()
border.All = PdfPen(Color.get_LightBlue())

#Iterate each row of grid
for i in range(grid.Rows.Count):
    pgr = grid.Rows[i]
    for j in range(pgr.Cells.Count):
      pgc = pgr.Cells[j]
      pgc.Style.Borders = border


#Draw the grid
grid.Draw(page, PointF(20.0,30.0))

#Save the pdf document
document.SaveToFile("BorderColor.pdf")

document.Dispose()