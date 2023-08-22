from spire.pdf.common import *
from spire.pdf import *


inputFile = "./Demos/Data/FillFormField.pdf"
outputFile = "FillFormField.pdf"

#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
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
#Save pdf document
doc.SaveToFile(outputFile)
doc.Close()

