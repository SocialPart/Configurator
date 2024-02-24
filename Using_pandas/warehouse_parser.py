from lxml import etree
import pandas as pd

path = '../Temp/etc/KC/warehouse.xml'

def parse_warehouse(path):
    warehouse = dict(points=pd.DataFrame(),
                 commands=pd.DataFrame())
    tree = etree.parse(path)
    root = tree.getroot()

    points_element = root.find('POINTS')
    commands_element = root.find('COMMANDS')

    for point_element in points_element.findall('POINT'):
        point_name = point_element.get('NAME')
        point_c = point_element.get('C')
        point_signal_type = point_element.get('SIGNAL_TYPE')
        point_naming = point_element.get('NAMING')
        point_lo = point_element.get('LO')
        point_hi = point_element.get('HI')
        point_formula = point_element.get('FORMULA')
        point_formula_time = point_element.get('FORMULA_TIME')
        point_aging = point_element.get('AGING')
        points_invert = point_element.get('INVERT')
        point = {'name': point_name, 'c': point_c, 'signal_type': point_signal_type, 'naming': point_naming,
                 'lo': point_lo, 'hi': point_hi, 'formula': point_formula,
                 'formula_time': point_formula_time, 'aging': point_aging, 'invert': points_invert}
        warehouse['points'] = warehouse['points']._append(point, ignore_index=True)

    warehouse['points'].set_index('name', inplace=True)

    for command_element in commands_element.findall('COMMAND'):
        command_name = command_element.get('NAME')
        command_c = command_element.get('C')
        command_signal_type = command_element.get('SIGNAL_TYPE')
        command_naming = command_element.get('NAMING')
        command_state = command_element.get('STATE')
        command_last = command_element.get('LAST')
        command_lock_cond_on = command_element.get('LOCK_COND_ON')
        command_lock_cond_off = command_element.get('LOCK_COND_OFF')
        command_trk = command_element.get('TRK')
        command_use_tracking = command_element.get('USE_TRACKING')
        command = {'name': command_name, 'c': command_c, 'signal_type': command_signal_type,
                   'naming': command_naming, 'state': command_state,
                   'last': command_last, 'lock_cond_on': command_lock_cond_on,
                   'lock_cond_off': command_lock_cond_off, 'trk': command_trk,
                   'use_tracking': command_use_tracking}
        warehouse['commands'] = warehouse['commands']._append(command, ignore_index=True)

    warehouse['commands'].set_index('name', inplace=True)

    return warehouse
# for i in warehouse.get('points'):
#     print(i.name)
s = parse_warehouse(path)

print(s['commands'].loc['KC.Kernel.Reboot']['naming'])
