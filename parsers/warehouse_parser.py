from lxml import etree
import models.warehouse_classes as warehouse_classes

path = '../Temp/etc/KC/warehouse.xml'

warehouse = dict(points=[], commands=[])

tree = etree.parse(path)
root = tree.getroot()

points_element = root.find('POINTS')
commands_element = root.find('COMMANDS')

for point_element in points_element.findall('POINT'):
    point_name = point_element.get('NAME')
    point_c = point_element.get('C')
    if point_c == '0':
        point_signal_type = point_element.get('SIGNAL_TYPE')
        point_naming = point_element.get('NAMING')
        point_lo = point_element.get('LO')
        point_hi = point_element.get('HI')
        point_formula = point_element.get('FORMULA')
        point_formula_time = point_element.get('FORMULA_TIME')
        point_aging = point_element.get('AGING')
        point = warehouse_classes.AnalogPoint(name=point_name, signal_type=point_signal_type,
                                              naming=point_naming, lo=point_lo,
                                              hi=point_hi, formula=point_formula,
                                              formula_time=point_formula_time, aging=point_aging)
        warehouse['points'].append(point)
    if point_c == '1':
        point_signal_type = point_element.get('SIGNAL_TYPE')
        point_naming = point_element.get('NAMING')
        point_formula = point_element.get('FORMULA')
        point_formula_time = point_element.get('FORMULA_TIME')
        point_aging = point_element.get('AGING')
        point_invert = point_element.get('INVERT')
        point = warehouse_classes.DiscretePoint(name=point_name, signal_type=point_signal_type,
                                                naming=point_naming, formula=point_formula,
                                                formula_time=point_formula_time, aging=point_aging,
                                                invert=point_invert)
        warehouse['points'].append(point)

for command_element in commands_element.findall('COMMAND'):
    command_name = command_element.get('NAME')
    command_signal_type = command_element.get('SIGNAL_TYPE')
    command_naming = command_element.get('NAMING')
    command_state = command_element.get('STATE')
    command_last = command_element.get('LAST')
    command_lock_cond_on = command_element.get('LOCK_COND_ON')
    command_lock_cond_off = command_element.get('LOCK_COND_OFF')
    command_trk = command_element.get('TRK')
    command_use_tracking = command_element.get('USE_TRACKING')
    command = warehouse_classes.CommandPoint(name=command_name, signal_type=command_signal_type,
                                             naming=command_naming, state=command_state,
                                             last=command_last, lock_cond_on=command_lock_cond_on,
                                             lock_cond_off=command_lock_cond_off, trk=command_trk,
                                             use_tracking=command_use_tracking)
    warehouse['commands'].append(command)

# for i in warehouse.get('points'):
#     print(i.name)
