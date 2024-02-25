# classes.py
import parsers

"""Описать классы и методы для работы с конфигуратором"""


class Warehouse:
    def __init__(self):
        self.warehouse = parsers.parse_warehouse()
        self.points = self.warehouse['points']
        self.commands = self.warehouse['commands']
        pass

    def add_discrete(self, name: str, c: str = '1', signal_type: str = '1', naming: str = None,
                     formula: str = None, formula_time: str = None, aging: str = None, invert: str = None):
        discrete = {'name': name, 'c': c, 'signal_type': signal_type, 'naming': naming,
                    'formula': formula, 'formula_time': formula_time, 'aging': aging, 'invert': invert}
        self.points.loc[name] = discrete

    def add_analog(self, name: str, c: str = '0', signal_type: str = '12', naming: str = None,
                   lo: str = None, hi: str = None, var: str = None, abs_var: str = None,
                   formula: str = None, formula_time: str = None, aging: str = None):
        analog = {'name': name, 'c': c, 'signal_type': signal_type, 'naming': naming,
                  'lo': lo, 'hi': hi, 'var': var, 'abs_var': abs_var,
                  'formula': formula, 'formula_time': formula_time, 'aging': aging}
        self.points.loc[name] = analog

    def add_command(self, name: str, c: str = '2', signal_type: str = '14', naming: str = None,
                    state: str = None, last: str = None, lock_cond_on: str = None, lock_cond_off: str = None,
                    trk: str = None, use_tracking: str = '0'):
        command = {'name': name, 'c': c, 'signal_type': signal_type, 'naming': naming,
                   'state': state, 'last': last, 'lock_cond_on': lock_cond_on, 'lock_cond_off': lock_cond_off,
                   'trk': trk, 'use_tracking': use_tracking}
        self.commands.loc[name] = command


class Kernel:
    def __init__(self):
        self.kernel = parsers.parse_kernel()
        self.points = self.kernel['points']
        self.commands = self.kernel['commands']
        pass
