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


"Ссылка на экземпляр в Warehouse для дополнительной информации и возможности конифгурирования"
def warehouse_point_link(tag, warehouse):
    for point_warehouse in warehouse['points']:
        if tag == point_warehouse.name:
            return point_warehouse
