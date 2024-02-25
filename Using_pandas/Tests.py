import parsers
import classes

"""Проверка корректности создания датафрейма Warehouse под Points"""

# wh = parsers.parse_warehouse()
# print(wh['points'])
# wh_filename = 'warehouse_pointsw.xlsx'
# wh['points'].to_excel(wh_filename)
# wh_command_filename = 'warehouse_commands.xlsx'
# wh['commands'].to_excel(wh_command_filename)

"""Проверка корректности создания датафрейма Kernel под Points"""

# ker = parsers.parse_kernel()
# print(ker['points'])
# ker_filename = 'kernel_points.xlsx'
# ker['points'].to_excel(ker_filename)

"Проверка конструктора экземпляра класса для Warehouse и проверка методов"

wh = classes.Warehouse()
print(wh)
print(wh.points)
wh.add_discrete(name='Testing')
wh_points_filename = 'wh_points.xlsx'
wh.points.to_excel(wh_points_filename)

