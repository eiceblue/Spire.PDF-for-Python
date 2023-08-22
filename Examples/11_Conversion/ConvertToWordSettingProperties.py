from spire.pdf.common import *
from spire.pdf import *

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