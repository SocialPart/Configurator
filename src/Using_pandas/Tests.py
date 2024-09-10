# Tests.py

import parsers
import tracemalloc
import classes
from memory_profiler import profile

"""Проверка корректности создания датафрейма Warehouse под Points"""

# wh = parsers.parse_warehouse()
# print(wh['points'])
# wh_filename = 'warehouse_pointsw.xlsx'
# wh['points'].to_excel(wh_filename)
# wh_command_filename = 'warehouse_commands.xlsx'
# wh['commands'].to_excel(wh_command_filename)

"""Проверка корректности создания датафрейма Kernel под Points"""

# ker = parsers.parsepython -m memory_profiler your_script.py_kernel()
# print(ker['points'])
# ker_filename = 'kernel_points.xlsx'
# ker['points'].to_excel(ker_filename)

"Проверка конструктора экземпляра класса для Warehouse и проверка методов"

# wh = classes.Warehouse()
# print(wh)
#
# wh.add_discrete(name='Testing')
# wh.add_analog(name='Testing_analog')
# wh.add_command(name='wh_command')
# wh_points_filename = 'wh_points.xlsx'
# wh_commands_filename = 'wh_commands.xlsx'
# wh.points.to_excel(wh_points_filename)
# wh.commands.to_excel(wh_commands_filename)
# print(wh.points)

"Проверка конструктора экземпляра классов для Kernel и проверка методов"

# ker = classes.Kernel()
#
# ker.add_point(name='PointTest')
# ker.add_command(name='CommandTest')
# ker_p_filename = 'ker_points.xlsx'
# ker_c_filename = 'ker_commands.xlsx'
# ker.points.to_excel(ker_p_filename)
# ker.commands.to_excel(ker_c_filename)

"""Проверка работы парсеров Warehouse, Kernel, iec101req и оценка затрачиваемой оперативной памяти (примерно 1,3 МБ)"""

tracemalloc.start()
warehouse = parsers.parse_warehouse()
kernel = parsers.parse_kernel()
iec101req = parsers.parse_iec101req()

#print(iec101req['slaves']['Группа 1']['devices'].iloc[5]['translation']['points'])
#tracemalloc.stop()

s = tracemalloc.get_traced_memory()
snap = tracemalloc.take_snapshot()
top_stats = snap.statistics('lineno')
print(top_stats)
print(s)
print(iec101req['slaves'])