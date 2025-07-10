from spire.pdf import *

def AppendAllText(fname: str, text: List[str]):
    fp = open(fname, "w")
    for s in text:
        fp.write(s + "\n")
    fp.close()

inputFile = "./Demos/Data/Extraction.pdf"

# Create a PDF document
doc = PdfDocument()
doc.LoadFromFile(inputFile)

# Create a buffer to store the extracted text
sbuffer = []
images = []#change:define an array of image objects for caching
# Iterate through each page in the document
for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)

    # Create a PdfTextExtractor object for the page
    pdfTextExtractor = PdfTextExtractor(page)

    # Create PdfTextExtractOptions object
    pdfTextExtractOptions = PdfTextExtractOptions()

    # Extract the text from the page
    sbuffer.append(pdfTextExtractor.ExtractText(pdfTextExtractOptions))
    # pictures 【change】
    imageHelper = PdfImageHelper()
    imageInfo = imageHelper.GetImagesInfo(page)#change:imageInfo = page.ImagesInfo
    for info in imageInfo:
        images.append(info.Image)

# Save the extracted text to a file
fileName = "Extraction.txt"
AppendAllText(fileName, sbuffer)

# Save the images from the page
# imageInfo = page.ImagesInfo
# for i in range(len(imageInfo)):
#     output = "Image-{0:d}.png".format(i)
#     imageInfo[i].Image.Save(output)
for index, img in enumerate(images):
    img_path = os.path.join("./Demos/Data", f"Image-{index}.png")
    img.Save(img_path)  
# Close the document
doc.Close()

