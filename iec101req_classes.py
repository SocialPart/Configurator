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
    def __init__(self, name, desc, disabled, station_address, common_address_of_asdu,
                 asdu_address_bytes, obj_address_bytes, cot_bytes, station_address_bytes,
                 interrogation_check, clock_sync, clock_sync_check, sleep):
        self.points = IEC101req_default_points
        self.commands = []
        self.name: str = ''
        self.disabled: int = 0
        self.station_address: int = 1
        self.common_address_of_asdu: int = 1
        self.asdu_address_bytes: int = 1
        self.obj_address_bytes: int = 2
        self.cot_bytes: int = 1
        self.station_address_bytes: int = 1
        self.interrogation_check: int = 60
        self.clock_sync: int = 1
        self.clock_sync_check: int = 60
        sel.sleep: int = 0

IEC101req_default_points = [IEC101_req_Point(name='Connect', address=0),
                            IEC101_req_Point(name='ActiveConnect', address=0)]
print(IEC101req_default_points[1].name)
