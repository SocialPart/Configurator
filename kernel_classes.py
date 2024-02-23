# kernel_classes.py


"""Создание классов для описания сигналов в kernel"""


class AnalogPoint:
    def __init__(self, name: str = '', signal_type: int = 10,
                 lo: int = None, hi: int = None, var: int = None,
                 abs_var: int = None, formula: str = None):
        self.name = name
        self.signal_type = signal_type
        self.lo = lo
        self.hi = hi
        self.var = var
        self.abs_var = abs_var
        self.formula = formula


class DiscretePoint:
    def __init__(self, name: str = '', signal_type: int = 1,
                 invert: int = None, formula: str = None, ):
        self.name = name
        self.signal_type = signal_type
        self.invert = invert
        self.formula = formula


class CommandPoint:
    def __init__(self, name: str = '', signal_type: int = 15,
                 trk: str = None, use_tracking: int = 0):
        self.name = name
        self.signal_type = signal_type
        self.trk = trk
        self.use_tracking = use_tracking
