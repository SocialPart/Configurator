from enum import Enum

"""
Общие типы данных для Warehouse, Kernel

"""

class SignalType(Enum): # Кодировка типов данных Warehouse
    NONE = 0
    BOOL = 1
    UINT8 = 2
    UINT16 = 3
    UINT32 = 4
    UINT64 = 5
    INT8 = 6
    INT16 = 7
    INT32 = 8
    INT64 = 9
    FLOAT = 10
    DOUBLE = 11
    STRING = 12
    TIME = 13
    CMD = 14
    SEL_EXEC = 15

class CType(Enum): # Поправить под С = 0,1,2.
    ANALOG = 0
    DISCRETE = 1
    COMMAND = 2