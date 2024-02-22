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

