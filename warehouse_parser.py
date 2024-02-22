from lxml import etree
import iec101req_classes
import defs

path = 'Temp/etc/KC/warehouse.xml'

tree = etree.parse(path)
root = tree.getroot()

points_element = root.find('POINTS')
commands_element = root.find('COMMANDS')

for point in points_element.findall('POINT'):
    print(point)