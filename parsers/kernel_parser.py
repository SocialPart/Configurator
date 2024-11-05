#kernel_parser.py
from lxml import etree
import models.kernel_classes as kernel_classes

path = '../Temp/etc/KC/kernel.xml'

kernel = dict(points=[], commands=[])

tree = etree.parse(path)
root = tree.getroot()

points_element = root.find('POINTS')
commands_element = root.find('COMMANDS')

