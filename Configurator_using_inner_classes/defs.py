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



def warehouse_link(element, point_tag, warehouse):
    if element.tag == 'POINT':
        for point_warehouse in warehouse['points']:
            if point_tag == point_warehouse.name:
                point_warehouse.source_link = element
                return point_warehouse
    if element.tag == 'COMMAND':
        for command_warehouse in warehouse['commands']:
            if point_tag == command_warehouse.name:
                command_warehouse.source_link = element
                return command_warehouse




