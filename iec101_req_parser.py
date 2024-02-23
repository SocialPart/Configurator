from lxml import etree
import iec101req_classes
from warehouse_parser import warehouse

import defs

path = 'Temp/etc/KC/iec101_req.xml'
initial_tag = 'IEC 60870-5-101 Req'

tree = etree.parse(path)
root = tree.getroot()
#print(root)
slaves_element = root.find('SLAVES')

slaves = []

for slave_element in slaves_element.findall('SLAVE'):
    slave_info = defs.parse_xml(slave_element)
    slave_name = slave_element.get('NAME')
    slave_tag = initial_tag + '.' + slave_name
    ds_sources_element = slave_element.find('DATA_SOURCES')
    data_sources_lst = []
    devices_element = slave_element.find('DEVICES')
    devices_lst = []
    slave = iec101req_classes.IEC101reqSlave(name=slave_name, data_sources=data_sources_lst, devices=devices_lst)
    slaves.append(slave)
    for ds_element in ds_sources_element.findall('DS'):
        ds_port = ds_element.get('PORT')
        ds_port_speed = ds_element.get('PORT_SPEED')
        ds_byte_reading = ds_element.get('BYTE_READING')
        ds_byte_reading_timeout = ds_element.get('BYTE_READING_TIMEOUT')
        ds_port_parity = ds_element.get('PORT_PARITY')
        ds_port_bytesize = ds_element.get('PORT_BYTESIZE')
        ds_port_stopbits = ds_element.get('PORT_STOPBITS')
        ds_balanced = ds_element.get('BALANCED')
        ds_retries = ds_element.get('RETRIES')
        ds_interleave = ds_element.get('INTERLEAVE')
        ds_response_to = ds_element.get('RESPONSE_TO')
        data_source = iec101req_classes.IEC101reqDataSource(port=ds_port, port_speed=ds_port_speed,
                                                            byte_reading=ds_byte_reading,
                                                            byte_reading_timeout=ds_byte_reading_timeout,
                                                            port_parity=ds_port_parity, port_bytesize=ds_port_bytesize,
                                                            port_stopbits=ds_port_stopbits, balanced=ds_balanced,
                                                            retries=ds_retries, interleave=ds_interleave,
                                                            responce_to=ds_response_to)
        data_sources_lst.append(data_source)

    for device_element in devices_element.findall('DEVICE'):
        points_element = device_element.find('POINTS')
        points_lst = []

        commands_element = device_element.find('COMMANDS')
        commands_lst = []

        device_name = device_element.get('NAME')
        device_tag = slave_tag + '.' + device_name
        device_desc = device_element.get('DESC')
        device_disabled = device_element.get('DISABLED')
        device_tz = device_element.get('TZ')
        device_station_address = device_element.get('STATION_ADDRESS')
        device_common_address_of_asdu = device_element.get('COMMON_ADDRESS_OF_ASDU')
        device_asdu_address_bytes = device_element.get('ASDU_ADDRESS_BYTES')
        device_obj_address_bytes = device_element.get('OBJ_ADDRESS_BYTES')
        device_cot_bytes = device_element.get('COT_BYTES')
        device_station_address_bytes = device_element.get('STATION_ADDRESS_BYTES')
        device_interrogation_check = device_element.get('INTERROGATION_CHECK')
        device_clock_sync = device_element.get('CLOCK_SYNC')
        device_clock_sync_check = device_element.get('CLOCK_SYNC_CHECK')
        device_sleep = device_element.get('SLEEP')
        device = iec101req_classes.IEC101reqDevice(points=points_lst, commands=commands_lst,
                                                   name=device_name, desc=device_desc,
                                                   disabled=device_disabled, tz=device_tz,
                                                   station_address=device_station_address,
                                                   common_address_of_asdu=device_common_address_of_asdu,
                                                   asdu_address_bytes=device_asdu_address_bytes,
                                                   obj_address_bytes=device_obj_address_bytes,
                                                   cot_bytes=device_cot_bytes,
                                                   station_address_bytes=device_station_address_bytes,
                                                   interrogation_check=device_interrogation_check,
                                                   clock_sync=device_clock_sync,
                                                   clock_sync_check=device_clock_sync_check, sleep=device_sleep)
        devices_lst.append(device)

        for point_element in points_element.findall('POINT'):
            point_name = point_element.get('NAME')
            point_tag = device_tag + '.' + point_name
            point_address = point_element.get('ADDRESS')
            point_warehouse_link = defs.warehouse_point_link(point_tag, warehouse)
            point = iec101req_classes.IEC101reqPoint(tag=point_tag, warehouse_link=point_warehouse_link,
                                                     name=point_name, address=point_address)
            points_lst.append(point)

        device.points = points_lst

        for command_element in commands_element.findall('COMMAND'):
            command_name = command_element.get('NAME')
            command_tag = device_tag + '.' + command_name
            command_address = command_element.get('ADDRESS')
            command_off_address = command_element.get('OFF_ADDRESS')
            command_qu = command_element.get('QU')
            command_common_address = command_element.get('COMMON_ADDRESS')
            command_type_id = command_element.get('TYPE_ID')
            command_signal_type = command_element.get('SIGNAL_TYPE')
            command_wait_a = command_element.get('WAIT_A')
            command = iec101req_classes.IEC101reqCommand(tag=command_tag, name=command_name, address=command_address,
                                                         off_address=command_off_address, qu=command_qu,
                                                         common_address=command_common_address, type_id=command_type_id,
                                                         signal_type=command_signal_type, wait_a=command_wait_a)
            commands_lst.append(command)

        device.commands = commands_lst

    slave.data_sources = data_sources_lst
    slave.devices = devices_lst

print(slaves[0].devices[1].points[1].tag)
print(slaves[0].devices[1].points[1].warehouse_link.name)
