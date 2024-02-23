# iec101req_classes.py

"""Создание класса для хранения данных клиента МЭК-101"""


class IEC101reqPoint:
    def __init__(self, warehouse_tag, warehouse_link, name: str = '', address: int = 0):
        self.warehouse_tag = warehouse_tag
        self.warehouse_link = warehouse_link
        self.to_warehouse_link = warehouse_link.source_link = self
        self.name = name
        self.address = address


class IEC101reqCommand:
    def __init__(self, warehouse_tag, warehouse_link, name: str = '', address: int = 0, off_address: int = 0,
                 qu: int = 0, common_address: int = 1, type_id: str = 'C_SC_NA_1',
                 signal_type: int = 14, wait_a: int = None):
        self.warehouse_tag = warehouse_tag
        self.warehouse_link = warehouse_link
        self.to_warehouse_link = warehouse_link.source_link = self
        self.name = name
        self.address = address
        self.off_address = off_address
        self.qu = qu
        self.common_address = common_address
        self.type_id = type_id
        self.signal_type = signal_type
        self.wait_a = wait_a


class IEC101reqDevice:
    def __init__(self, points: list = None, commands: list = None, name: str = '', desc: str = '',
                 disabled: int = 0, station_address: int = 1, tz: int = None,
                 common_address_of_asdu: int = 1, asdu_address_bytes: int = 1, obj_address_bytes: int = 2,
                 cot_bytes: int = 1, station_address_bytes: int = 1, interrogation_check: int = 60, InterrogationType: str = None,
                 clock_sync: int = 1, clock_sync_check: int = 60, ClockSyncType: str = None,
                sleep: int = 0):
        self.points = points
        self.commands = commands
        self.name = name
        self.desc = desc
        self.disabled = disabled
        self.station_address = station_address
        self.tz = tz
        self.common_address_of_asdu = common_address_of_asdu
        self.asdu_address_bytes = asdu_address_bytes
        self.obj_address_bytes = obj_address_bytes
        self.cot_bytes = cot_bytes
        self.station_address_bytes = station_address_bytes
        self.interrogation_check = interrogation_check
        self.interrogation_type = InterrogationType
        self.clock_sync = clock_sync
        self.clock_sync_check = clock_sync_check
        self.clock_sync_type = ClockSyncType
        self.sleep = sleep


class IEC101reqDataSource:
    def __init__(self, port: str = '', port_speed: int = 9600, byte_reading: int = 0, byte_reading_timeout: int = 100,
                 port_parity: int = 0, port_bytesize: int = 8, port_stopbits: int = 0, balanced: int = 0,
                 retries: int = 3, interleave: int = 100, responce_to: int = 500):
        self.port = port
        self.port_speed = port_speed
        self.byte_reading = byte_reading
        self.byte_reading_timeout = byte_reading_timeout
        self.port_parity = port_parity
        self.port_bytesize = port_bytesize
        self.port_stopbits = port_stopbits
        self.balanced = balanced
        self.retries = retries
        self.interleave = interleave
        self.responce_to = responce_to


class IEC101reqSlave:
    def __init__(self, name: str = '', data_sources: list = None, devices: list = None):
        self.data_sources = data_sources
        self.devices = devices
        self.name = name


"""Дефолтные каналы будут добавляться только при создании нового клиента, 
в остальном же - парситься из xml-файла"""

# IEC101req_default_points = [IEC101reqPoint(name='Connect', address=0),
#                             IEC101reqPoint(name='ActiveConnect', address=0)]

# s = IEC101req_Device(name='ss')
# s.points.append(IEC101req_Point(name='Test', address=123))
# print(s.points)
