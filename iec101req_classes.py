#iec101reqclasses.py

class IEC101_req_Point:
    def __init__(self, name: str = '', address:int =0):
        self.name = name
        self.address = address

class IEC101_req_Command:
    def __init__(self, name: str = '', address: int = 0, off_address: int = 0,
                 qu: int = 0, common_address: int = 1, type_id: str = 'C_SC_NA_1',
                 signal_type: int = 14, wait_a: int = 0):
        self.name = name
        self.address = address
        self.off_address = off_address
        self.qu = qu
        self.common_address = common_address
        self.type_id = type_id
        self.signal_type = signal_type
        self.wait_a = wait_a

class IEC101_req_Device:
    def __init__(self, name: str = '', desc: str = '', disabled: int = 0, station_address: int = 1,
                 common_address_of_asdu: int = 1, asdu_address_bytes: int = 1, obj_address_bytes: int = 2,
                 cot_bytes: int = 1, station_address_bytes: int = 1, interrogation_check: int = 60,
                 clock_sync: int = 1, clock_sync_check: int = 60, sleep: int = 0):
        self.points = IEC101req_default_points
        self.commands = []
        self.name = name
        self.desc = desc
        self.disabled = disabled
        self.station_address = station_address
        self.common_address_of_asdu = common_address_of_asdu
        self.asdu_address_bytes = asdu_address_bytes
        self.obj_address_bytes = obj_address_bytes
        self.cot_bytes = cot_bytes
        self.station_address_bytes = station_address_bytes
        self.interrogation_check = interrogation_check
        self.clock_sync = clock_sync
        self.clock_sync_check = clock_sync_check
        self.sleep = sleep

IEC101req_default_points = [IEC101_req_Point(name='Connect', address=0),
                            IEC101_req_Point(name='ActiveConnect', address=0)]

s = IEC101_req_Device(name='ss')
s.points.append(IEC101_req_Point(name='Test', address=123))
print(s.points)
