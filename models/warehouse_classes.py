# warehouse_classes.py
from dataclasses import dataclass, field # Используем dataclasses для более удобного задания классов, полей и т.д
from models.CommonTypes import SignalType, CType # Описание типов сигналов согласно кодам

"""Классы для хранения тэгов трансляции"""

"""Явное задание пустой строки по дефолту будет соответствовать
полю, которое присутствует в warehouse даже при отсутствии там значения
если поле None, то данный атрибут не попадет в warehouse.xml"""

"""Для реализации менеджера объектов нужно будет удалить source link"""

@dataclass
class AnalogPoint:
    source_link: str = field(default=None)
    name: str = field(default="")
    c: CType = field(default=CType.ANALOG)
    signal_type: SignalType = field(default=SignalType.FLOAT)
    naming: str = field(default="")
    lo: int = field(default=None)
    hi: int = field(default=None)
    formula: str = field(default=None)
    formula_time: str = field(default=None)
    aging: int = field(default=None)


@dataclass
class DiscretePoint:
    source_link: str = field(default=None)
    name: str = field(default="")
    c: CType = field(default=CType.DISCRETE)
    signal_type: SignalType = field(default=SignalType.BOOL)
    naming: str = field(default="")
    formula: str = field(default=None)
    formula_time: str = field(default=None)
    aging: int = field(default=None)
    invert: int = field(default=None)

@dataclass
class CommandPoint:
    source_link: str = field(default=None)
    name: str = field(default="")
    c: CType = field(default=CType.COMMAND)
    signal_type: SignalType = field(default=SignalType.SEL_EXEC)
    naming: str = field(default="")
    state: str = field(default=None)
    last: str = field(default=None)
    lock_cond_on: str = field(default=None)
    lock_cond_off: str = field(default=None)
    trk: str = field(default="")
    use_tracking: int = field(default=0)
