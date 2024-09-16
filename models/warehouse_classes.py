# warehouse_classes.py
from dataclasses import dataclass, field # Используем dataclasses для более удобного задания классов, полей и т.д
from CommonTypes import SignalType, CType # Описание типов сигналов согласно кодам


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
