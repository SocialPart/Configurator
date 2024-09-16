# kernel_classes.py
from dataclasses import dataclass, field
from CommonTypes import SignalType, CType


"""Создание классов для описания сигналов в kernel"""

@dataclass
class AnalogPoint:
    name: str = ""
    signal_type: SignalType = field(default=SignalType.FLOAT)
    lo: int = field(default=None)
    hi: int = field(default=None)
    var: int = field(default=None)
    abs_var: int = field(default=None)
    formula: str = field(default=None)

    # def __init__(self, name: str = '', signal_type: int = 10,
    #              lo: int = None, hi: int = None, var: int = None,
    #              abs_var: int = None, formula: str = None):
    #     self.name = name
    #     self.signal_type = signal_type
    #     self.lo = lo
    #     self.hi = hi
    #     self.var = var
    #     self.abs_var = abs_var
    #     self.formula = formula

@dataclass
class DiscretePoint:
    name: str = ""
    signal_type: SignalType = field(default=SignalType.BOOL)
    invert: int = field(default=None)
    formula: str = field(default=None)

    # def __init__(self, name: str = '', signal_type: int = 1,
    #              invert: int = None, formula: str = None, ):
    #     self.name = name
    #     self.signal_type = signal_type
    #     self.invert = invert
    #     self.formula = formula

@dataclass
class CommandPoint:
    name: str = ""
    signal_type: SignalType = field(default=SignalType.SEL_EXEC)
    trk: str = field(default=None)
    use_tracking: int = field(default=None)
    # def __init__(self, name: str = '', signal_type: int = 15,
    #              trk: str = None, use_tracking: int = 0):
    #     self.name = name
    #     self.signal_type = signal_type
    #     self.trk = trk
    #     self.use_tracking = use_tracking
