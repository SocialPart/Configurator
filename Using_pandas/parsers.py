from lxml import etree
import pandas as pd
import numpy as np

# from memory_profiler import profile
# import defs

"""Создание парсера warehouse. """


def parse_warehouse(path: str = '../Temp/etc/KC/warehouse.xml') -> dict:
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
        point_var = point_element.get('VAR')
        point_abs_var = point_element.get('ABS_VAR')
        point_formula = point_element.get('FORMULA')
        point_formula_time = point_element.get('FORMULA_TIME')
        point_aging = point_element.get('AGING')
        points_invert = point_element.get('INVERT')

        # Проверка типа сигнала для установки в несоответствующих атрибутах NaN
        if point_c == '0':
            points_invert = np.NAN
        if point_c == '1':
            point_lo = np.NAN
            point_hi = np.NAN
            point_var = np.NAN
            point_abs_var = np.NAN
        point = {'name': point_name, 'c': point_c, 'signal_type': point_signal_type, 'naming': point_naming,
                 'lo': point_lo, 'hi': point_hi, 'var': point_var, 'abs_var': point_abs_var,
                 'formula': point_formula, 'formula_time': point_formula_time, 'aging': point_aging,
                 'invert': points_invert}
        warehouse['points'] = warehouse['points']._append(point, ignore_index=True)

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

    warehouse['points'].set_index('name', inplace=True)
    warehouse['commands'].set_index('name', inplace=True)

    return warehouse


"""В отличии от Warehouse отдельно добавлять Points и делить их на ТС и ТИ по параметру С не получится
Добавляем все каналы Point. По существу парсить и создавать класс под Kernel для экспорта в xlsx не требуется 
(только далее при работе конфигуратором)"""


def parse_kernel(path: str = '../Temp/etc/KC/kernel.xml') -> dict:
    kernel = dict(points=pd.DataFrame(),
                  commands=pd.DataFrame())
    tree = etree.parse(path)
    root = tree.getroot()

    points_element = root.find('POINTS')
    commands_element = root.find('COMMANDS')

    for point_element in points_element.findall('POINT'):
        point_name = point_element.get('NAME')
        point_signal_type = point_element.get('SIGNAL_TYPE')
        points_invert = point_element.get('INVERT')
        point_lo = point_element.get('LO')
        point_hi = point_element.get('HI')
        point_var = point_element.get('VAR')
        point_abs_var = point_element.get('ABS_VAR')
        point_formula = point_element.get('FORMULA')

        point = {'name': point_name, 'signal_type': point_signal_type, 'invert': points_invert,
                 'lo': point_lo, 'hi': point_hi, 'var': point_var, 'abs_var': point_abs_var,
                 'formula': point_formula}
        kernel['points'] = kernel['points']._append(point, ignore_index=True)

    for command_element in commands_element.findall('COMMAND'):
        command_name = command_element.get('NAME')
        command_signal_type = command_element.get('SIGNAL_TYPE')
        command_trk = command_element.get('TRK')
        command_use_tracking = command_element.get('USE_TRACKING')
        command = {'name': command_name, 'signal_type': command_signal_type,
                   'trk': command_trk, 'use_tracking': command_use_tracking}
        kernel['commands'] = kernel['commands']._append(command, ignore_index=True)

    kernel['points'].set_index('name', inplace=True)
    kernel['commands'].set_index('name', inplace=True)

    return kernel


def parse_iec101req(path: str = '../Temp/etc/KC/iec101_req.xml') -> dict:
    iec101req = dict(slaves=dict())
    initial_tag = 'IEC 60870-5-101 Req'
    tree = etree.parse(path)
    root = tree.getroot()
    slaves_element = root.find('SLAVES')

    for slave_element in slaves_element.findall('SLAVE'):
        slave_name = slave_element.get('NAME')

        # Создание общей структуры данных под клиент

        iec101req['slaves'][slave_name] = dict(data_sources=pd.DataFrame(),
                                               devices=pd.DataFrame())
        # print(iec101req['slaves'][slave_name]['data_sources'])
        slave_tag = initial_tag + '.' + slave_name

        ds_sources_element = slave_element.find('DATA_SOURCES')
        devices_element = slave_element.find('DEVICES')

        # Ввел переменные для сокращенного обращения к атрибутам
        slave = iec101req['slaves'][slave_name]

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

            d_s = {'port': ds_port, 'port_speed': ds_port_speed, 'byte_reading': ds_byte_reading,
                   'byte_reading_timeout': ds_byte_reading_timeout, 'port_parity': ds_port_parity,
                   'port_bytesize': ds_port_bytesize, 'port_stopbits': ds_port_stopbits, 'balanced': ds_balanced,
                   'retries': ds_retries, 'interleave': ds_interleave, 'responce_to': ds_response_to}

            slave['data_sources'] = slave['data_sources']._append(d_s, ignore_index=True)

        slave['data_sources'].set_index('port', inplace=True)
        # print(slave['data_sources'])

        for device_element in devices_element.findall('DEVICE'):
            points_element = device_element.find('POINTS')
            commands_element = device_element.find('COMMANDS')

            # Определение структуры трансляции модуля
            device_translation = dict(points=pd.DataFrame(), commands=pd.DataFrame())

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

            dev_dict = {'name': device_name, 'desc': device_desc, 'disabled': device_disabled, 'tz': device_tz,
                        'station_address': device_station_address,
                        'common_address_of_asdu': device_common_address_of_asdu,
                        'asdu_address_bytes': device_asdu_address_bytes,
                        'obj_address_bytes': device_obj_address_bytes, 'cot_bytes': device_cot_bytes,
                        'station_address_bytes': device_station_address_bytes,
                        'interrogation_check': device_interrogation_check,
                        'clock_sync': device_clock_sync, 'clock_sync_check': device_clock_sync_check,
                        'sleep': device_sleep, 'translation': device_translation}

            slave['devices'] = slave['devices']._append(dev_dict, ignore_index=True)

            # Проиндексировал поиск по имени, т.к. в трансляции оно уникальное для Группы

            slave['devices'].set_index('name', inplace=True)

            # Ввел переменную для укорочения

            translation = slave['devices'].iloc[-1]['translation']

            for point_element in points_element.findall('POINT'):
                point_name = point_element.get('NAME')
                point_tag = str(device_tag + '.' + point_name)
                point_address = point_element.get('ADDRESS')
                point_dict = {'name': point_name, 'address': point_address, 'warehouse_tag': point_tag}

                # Остановился здесь, слишком длинные ссылки получаются, надо оптимизировать
                translation['points'] = translation['points']._append(point_dict, ignore_index=True)

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
                command_dict = {'warehouse_tag': command_tag, 'name': command_name, 'address': command_address,
                                'off_address': command_off_address, 'qu': command_qu,
                                'common_address': command_common_address, 'type_id': command_type_id,
                                'signal_type': command_signal_type, 'wait_a': command_wait_a}

                translation['commands'] = translation['commands']._append(command_dict, ignore_index=True)

            # Поиск в датафрейме будет по тэгу в Warehouse

            translation['points'].set_index('warehouse_tag', inplace=True)
            translation['commands'].set_index('warehouse_tag', inplace=True)

    return iec101req
