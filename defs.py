#defs.py

"""Рекурсивная функция, которая вытаскивает элементы и их атрибуты из дерева"""


def parse_xml(element):
    if len(element) == 0:
        return element.text.strip() if element.text else None
    else:
        result = {}
        for child in element:
            result[child.tag] = parse_xml(child)
        return result


"Ссылка на экземпляр Point в Warehouse для дополнительной информации и возможности конфигурирования" \
"Также можно использовать и для Kernel если он имеет вид словаря с Points и Commands"


def warehouse_point_link(element, point_tag, warehouse):
    for point_warehouse in warehouse['points']:
        if point_tag == point_warehouse.name:
            point_warehouse.source_link = element
            return point_warehouse

"Ссылка на экземпляр Command в Warehouse для дополнительной информации и возможности конфигурирования"


def warehouse_command_link(element, command_tag, warehouse):
    #print(element)
    for command_warehouse in warehouse['commands']:
        #print(command_warehouse.name)
        if command_tag == command_warehouse.name:
            command_warehouse.source_link = element
            return command_warehouse