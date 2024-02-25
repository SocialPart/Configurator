import parsers
#import classes

# Проверка корректности создания датафрейма Warehouse под Points
wh = parsers.parse_warehouse()
print(wh['points'])
wh_filename = 'warehouse_pointsw.xlsx'
wh['points'].to_excel(wh_filename)

# Проверка корректности создания датафрейма Kernel под Points
ker = parsers.parse_kernel()
print(ker['points'])
ker_filename = 'kernel_points.xlsx'
ker['points'].to_excel(ker_filename)