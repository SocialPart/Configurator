# warehouse_classes.py
from dataclasses import dataclass, field # Используем dataclasses для более удобного задания классов, полей и т.д
from enum import Enum

# Описание типов сигналов согласно кодам

class CType(Enum): # Поправить под С = 0,1,2. Сделать для типов данных (bool, int и тд)
    ANALOG = 0
    DISCRETE = 1
    COMMAND = 2

class SignalType(Enum): # Поправить под С = 0,1,2. Сделать для типов данных (bool, int и тд)
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

#Используем шаблон для базового Point, чтобы не повторяться в коде (принцип DRY - don't repeat yourself)
#Остальные классы будем наследовать от него

@dataclass
class BasePoint:
    source_link: str = None
    name: str = ""
    signal_type: int = 0
    naming: str = ""

@dataclass
class AnalogPoint:
    source_link: str = None
    name: str = ""
    c: CType = field(default=CType.ANALOG)
    signal_type: SignalType = field(default=SignalType.FLOAT)
    naming: str = ""
    lo: int = field(default=None)
    hi: int = field(default=None)
    formula: str = field(default=None)
    formula_time: str = field(default=None)
    aging: int = field(default=None)


@dataclass
class DiscretePoint:
    source_link: str = None
    name: str = ""
    c: CType = field(default=CType.DISCRETE)
    signal_type: SignalType = field(default=SignalType.BOOL)
    naming: str = ""
    formula: str = field(default=None)
    formula_time: str = field(default=None)
    aging: int = field(default=None)
    invert: int = field(default=None)

@dataclass
class CommandPoint:
    source_link: str = None
    name: str = ""
    c: CType = field(default=CType.COMMAND)
    signal_type: SignalType = field(default=SignalType.SEL_EXEC)
    naming: str = ""
    state: str = field(default=None)
    last: str = field(default=None)
    lock_cond_on: str = field(default=None)
    lock_cond_off: str = field(default=None)
    trk: str = field(default=None)
    use_tracking: int = field(default=0)

# class AnalogPoint:
#     def __init__(self, source_link: str = None, name: str = '', signal_type: int = 10, naming: str = '',
#                  lo: int = None, hi: int = None, formula: str = None,
#                  formula_time: str = None, aging: int = None):
#         self.source_link = source_link
#         self.name = name
#         self.c = 0
#         self.signal_type = signal_type
#         self.naming = naming
#         self.lo = lo
#         self.hi = hi
#         self.formula = formula
#         self.formula_time = formula_time
#         self.aging = aging


# class DiscretePoint:
#     def __init__(self, source_link: str = None, name: str = '', signal_type: int = 1, naming: str = '',
#                  formula: str = None, formula_time: str = None, aging: int = None,
#                  invert: int = None):
#         self.source_link = source_link
#         self.name = name
#         self.c = 1
#         self.signal_type = signal_type
#         self.naming = naming
#         self.formula = formula
#         self.formula_time = formula_time
#         self.aging = aging
#         self.invert = invert


# class CommandPoint:
#     def __init__(self, source_link: str = None, name: str = '', signal_type: int = 15, naming: str = '',
#                  state: str = None, last: str = None, lock_cond_on: str = None,
#                  lock_cond_off: str = None, trk: str = None, use_tracking: int = 0):
#         self.source_link = source_link
#         self.name = name
#         self.c = 2
#         self.signal_type = signal_type
#         self.naming = naming
#         self.state = state
#         self.last = last
#         self.lock_cond_on = lock_cond_on
#         self.lock_cond_off = lock_cond_off
#         self.trk = trk
#         self.use_tracking = use_tracking


