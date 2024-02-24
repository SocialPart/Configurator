import pandas as pd

path = '../Temp/etc/KC/iec101_req.xml'
xml_data = pd.read_xml(path)

print(xml_data)
