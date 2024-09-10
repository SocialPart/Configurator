from openpyxl import Workbook
import parsers

iec101req = parsers.parse_iec101req()
warehouse = parsers.parse_warehouse()
kernel = parsers.parse_kernel()
print(iec101req['slaves'])

# Создаем новую книгу Excel
for slave in iec101req['slaves'].keys():
    print(slave)
    wb = Workbook()

    # Выбираем активный лист
    ws = wb.active
    ws.title = 'Клиент101Клиент101Клиент101'

    # Добавляем данные в несколько строк
    data = [
        ['Header 1', 'Header 2', 'Header 3'],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    for row in data:
        ws.append(row)

    # Группируем строки с 2-й по 4-ю
    ws.row_dimensions.group(start=2, end=5, hidden=True)

    # Добавляем дополнительные строки в группу
    # for i in range(2, 8):
    #     ws.append([1, 2, 3])
    #     ws.row_dimensions.group(i)

    # Сохраняем книгу
    wb.save(f"{slave['name']}.xlsx")
