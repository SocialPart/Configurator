# warehouse_classes.py

class AnalogPoint:
    def __init__(self, source_link: str = None, name: str = '', signal_type: int = 10, naming: str = '',
                 lo: int = None, hi: int = None, formula: str = None,
                 formula_time: str = None, aging: int = None):
        self.source_link = source_link
        self.name = name
        self.c = 0
        self.signal_type = signal_type
        self.naming = naming
        self.lo = lo
        self.hi = hi
        self.formula = formula
        self.formula_time = formula_time
        self.aging = aging


class DiscretePoint:
    def __init__(self, source_link: str = None, name: str = '', signal_type: int = 1, naming: str = '',
                 formula: str = None, formula_time: str = None, aging: int = None,
                 invert: int = None):
        self.source_link = source_link
        self.name = name
        self.c = 1
        self.signal_type = signal_type
        self.naming = naming
        self.formula = formula
        self.formula_time = formula_time
        self.aging = aging
        self.invert = invert


class CommandPoint:
    def __init__(self, source_link: str = None, name: str = '', signal_type: int = 15, naming: str = '',
                 state: str = None, last: str = None, lock_cond_on: str = None,
                 lock_cond_off: str = None, trk: str = None, use_tracking: int = 0):
        self.source_link = source_link
        self.name = name
        self.c = 2
        self.signal_type = signal_type
        self.naming = naming
        self.state = state
        self.last = last
        self.lock_cond_on = lock_cond_on
        self.lock_cond_off = lock_cond_off
        self.trk = trk
        self.use_tracking = use_tracking


