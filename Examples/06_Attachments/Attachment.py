from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/Attachment.pdf"
outputFile = "Attachment.pdf"

#Create a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
page = doc.Pages[0]
y = 320.0
#Title
brush1 = PdfBrushes.get_CornflowerBlue()
font1 = PdfTrueTypeFont("Arial", 18.0, PdfFontStyle.Bold,True)
format1 = PdfStringFormat(PdfTextAlignment.Center)
page.Canvas.DrawString("Attachment", font1, brush1, page.Canvas.ClientSize.Width / float(2), y, format1)
y = y + font1.MeasureString("Attachment", format1).Height
y = y + 10
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
x = 50.0
font2 = PdfTrueTypeFont("Arial", 14.0, PdfFontStyle.Bold,True)
location = PointF(x, y)
label = "Sales Report Chart"
data = Stream("./Demos/Data/SalesReportChart.png" )
size = font2.MeasureString(label)
bounds = RectangleF(location, size)
page.Canvas.DrawString(label, font2, PdfBrushes.get_DarkOrange(), bounds)
bounds = RectangleF(bounds.Right +3, bounds.Top, font2.Height / float(2), font2.Height)
#Create a PdfAttachmentAnnotation 
annotation1 = PdfAttachmentAnnotation(bounds, "SalesReportChart.png", data)
annotation1.Color = PdfRGBColor(Color.get_Teal())
annotation1.Flags = PdfAnnotationFlags.ReadOnly
annotation1.Icon = PdfAttachmentIcon.Graph
annotation1.Text = "Sales Report Chart"
#Add the annotation1
page.AnnotationsWidget.Add(annotation1)
y = y + size.Height + 3
location = PointF(x, y)
label = "Science Personification Boston"
data = Stream("./Demos/Data/SciencePersonificationBoston.jpg" )
size = font2.MeasureString(label)
bounds = RectangleF(location, size)
page.Canvas.DrawString(label, font2, PdfBrushes.get_DarkOrange(), bounds)
bounds = RectangleF(bounds.Right + 3, bounds.Top, font2.Height / float(2), font2.Height)
annotation2 = PdfAttachmentAnnotation(bounds, "SciencePersonificationBoston.jpg", data)
annotation2.Color = PdfRGBColor(Color.get_Orange())
annotation2.Flags = PdfAnnotationFlags.NoZoom
annotation2.Icon = PdfAttachmentIcon.PushPin
annotation2.Text = "SciencePersonificationBoston.jpg, from Wikipedia, the free encyclopedia"
page.AnnotationsWidget.Add(annotation2)
y = y + size.Height + 2
location = PointF(x, y)
label = "Picture of Science"
data = Stream("./Demos/Data/Wikipedia_Science.png" )
size = font2.MeasureString(label)
bounds = RectangleF(location, size)
page.Canvas.DrawString(label, font2, PdfBrushes.get_DarkOrange(), bounds)
bounds = RectangleF(bounds.Right + 3, bounds.Top, font2.Height / float(2), font2.Height)
annotation3 = PdfAttachmentAnnotation(bounds, "Wikipedia_Science.png", data)
annotation3.Color = PdfRGBColor(Color.get_SaddleBrown())
annotation3.Flags = PdfAnnotationFlags.Locked
annotation3.Icon = PdfAttachmentIcon.Tag
annotation3.Text = "Wikipedia_Science.png, from Wikipedia, the free encyclopedia"
page.AnnotationsWidget.Add(annotation3)
y = y + size.Height + 2
location = PointF(x, y)
label = "PT_Serif-Caption-Web-Regular Font"
data = Stream("./Demos/Data/PT_Serif-Caption-Web-Regular.ttf" )
size = font2.MeasureString(label)
bounds = RectangleF(location, size)
page.Canvas.DrawString(label, font2, PdfBrushes.get_DarkOrange(), bounds)
bounds = RectangleF(bounds.Right + 3, bounds.Top, font2.Height / float(2), font2.Height)
annotation4 = PdfAttachmentAnnotation(bounds, "PT_Serif-Caption-Web-Regular.ttf", data)
annotation4.Color = PdfRGBColor(Color.get_CadetBlue())
annotation4.Flags = PdfAnnotationFlags.NoRotate
annotation4.Icon = PdfAttachmentIcon.Paperclip
annotation4.Text = "PT_Serif-Caption-Web-Regular, from https://company.paratype.com"
page.AnnotationsWidget.Add(annotation4)
y = y + size.Height + 2
#Save pdf file
doc.SaveToFile(outputFile)
doc.Close()

