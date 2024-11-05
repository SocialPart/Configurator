# iec101req_classes.py
from dataclasses import dataclass, field
from models.CommonTypes import SignalType, CType
from email.policy import default

"""
Файл для хранения результатов парсинга конфигурационного файла
клиента МЭК-101. Реализована иерархическая система (основываясь на структуре xml)
"""


"""Создание класса для хранения данных клиента МЭК-101"""

@dataclass
class IEC101reqPoint:
    warehouse_tag: any
    warehouse_link: any
    name: str = field(default=None)
    address: int = field(default=0)

    """Добавлен метод для связи с тэгом Warehouse, после создания экземпляра 
    IEC101reqPoint"""
    def __post_init__(self):
        self.to_warehouse_link = self.warehouse_link.source_link = self


@dataclass
class IEC101reqCommand:
    warehouse_tag: any
    warehouse_link: any
    name: str = field(default=None)
    address: int = field(default=0)
    off_address: str = field(default=0)
    qu: int = field(default=0)
    common_address: int = field(default=1)
    type_id: str = field(default='C_SC_NA_1')
    signal_type: SignalType = field(default=SignalType.CMD)
    wait_a: int = field(default=0)

    def __post_init__(self):
        self.to_warehouse_link = self.warehouse_link.source_link = self

@dataclass
class IEC101reqDevice:
    points: list = field(default_factory=list)
    commands: list = field(default_factory=list)
    points_map: dict = field(default_factory=dict)
    commands_map: dict = field(default_factory=dict)
    name: str = field(default="")
    desc: str = field(default="")
    disabled: int = field(default=0)
    station_address: int = field(default=1)
    tz: int = field(default=None)
    common_address_of_asdu : int = field(default=1)
    asdu_address_bytes : int = field(default=1)
    obj_address_bytes : int = field(default=2)
    cot_bytes : int = field(default=1)
    station_address_bytes : int = field(default=1)
    interrogation_check : int = field(default=60)
    interrogation_type : str = field(default="")
    clock_sync : int = field(default=1)
    clock_sync_check : int = field(default=60)
    clock_sync_type : int = field(default=None)
    sleep : int = field(default=10)

@dataclass
class IEC101reqDataSource:
    port: str = field(default=None)
    port_speed: int = field(default=9600)
    byte_reading: int = field(default=1)
    byte_reading_timeout: int = field(default=100)
    port_parity: int = field(default=0)
    port_bytesize: int = field(default=8)
    port_stopbits: int = field(default=0)
    balanced: int = field(default=0)
    retries: int = field(default=3)
    interleave: int = field(default=100)
    responce_to: int = field(default=500)

@dataclass
class IEC101reqSlave:
    data_sources = data_sources
    devices : list = field(default_factory=list)
    devices_map : dict = field(default_factory=dict)
    name : str = field(default="")

# class IEC101reqDataSource:
#     def __init__(self, port: str = '', port_speed: int = 9600, byte_reading: int = 0, byte_reading_timeout: int = 100,
#                  port_parity: int = 0, port_bytesize: int = 8, port_stopbits: int = 0, balanced: int = 0,
#                  retries: int = 3, interleave: int = 100, responce_to: int = 500):
#         self.port = port
#         self.port_speed = port_speed
#         self.byte_reading = byte_reading
#         self.byte_reading_timeout = byte_reading_timeout
#         self.port_parity = port_parity
#         self.port_bytesize = port_bytesize
#         self.port_stopbits = port_stopbits
#         self.balanced = balanced
#         self.retries = retries
#         self.interleave = interleave
#         self.responce_to = responce_to


# class IEC101reqSlave:
#     def __init__(self, name: str = '', data_sources: list = None, devices: list = None):
#         self.data_sources = data_sources
#         self.devices = devices
#         self.name = name


"""Дефолтные каналы будут добавляться только при создании нового клиента, 
в остальном же - парситься из xml-файла"""

# IEC101req_default_points = [IEC101reqPoint(name='Connect', address=0),
#                             IEC101reqPoint(name='ActiveConnect', address=0)]


