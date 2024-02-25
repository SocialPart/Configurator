import parsers
#import classes

# Проверка корректности создания датафрейма Warehouse под Points
s = parsers.parse_warehouse()
print(s['points'])
filename = 'warehouse_points.xlsx'
s['points'].to_excel(filename)