# xml
# xml uzywa tagow

from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)
productChild = root.createElement('product')
productChild.setAttribute("name", "Raj")
xml.appendChild(productChild)
xml_str = root.toprettyxml(indent="\t")
print(xml_str)

save_path = "raj.xml"
with open(save_path, "w") as f:
   f.write(xml_str)

