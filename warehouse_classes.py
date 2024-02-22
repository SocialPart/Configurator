# warehouse_classes.py


class AnalogPoint:
    def __init__(self, name: str = '', signal_type: int = 10, naming: str = '',
                 lo: int = None, hi: int = None, formula=None,
                 formula_time: str = None, aging: int = None):
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
    def __init__(self, name: str = '', signal_type: int = 1, naming: str = '',
                 formula: str = None, formula_time: str = None, aging: int = None,
                 invert: int = None):
        self.name = name
        self.c = 1
        self.signal_type = signal_type
        self.naming = naming
        self.formula = formula
        self.formula_time = formula_time
        self.aging = aging
        self.invert = invert

class CommandPoint:
    def __init__(self):




s = AnalogPoint()
print(s.c)
