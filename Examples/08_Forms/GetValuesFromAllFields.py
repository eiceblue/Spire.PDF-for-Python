from spire.pdf.common import *
from spire.pdf import *

inputFile = "./Demos/Data/AllFields.pdf"
outputFile = "GetAllValues.txt"

#Load a pdf document
doc = PdfDocument()
doc.LoadFromFile(inputFile)
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
#Save the result file
f2=open(outputFile,'w', encoding='UTF-8')
for item in sb:
        f2.write(item)
f2.close()
doc.Close()


