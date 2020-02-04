# частично справился с заданием
import xml.etree.ElementTree
import json

# строка с xml
xml_string = '<root><element1 /><element2 />'
+ '<element3><element4 /></element3></root>'


# функция, возвращяющая лист тэгов дочерних элементов
def children(root):
    list_of_children = []
    for i in list(root):
        list_of_children.append(i.tag)
    return list_of_children


# главная функция
# рекурсивно складыающая словарь
def make_dict_from_tree(element_tree):
    def internal_iter(tree, accum):
        global count  # счетчик
        count = 0
        if tree is None:
            return accum

        if list(tree):
            accum[tree.tag] = {}
            for each in list(tree):
                result = internal_iter(each, {})
                if each.tag in accum[tree.tag]:
                    if not isinstance(accum[tree.tag][each.tag], list):
                        accum[tree.tag][each.tag] = children(accum[tree.tag])

                    accum[tree.tag][each.tag].append(result[each.tag])
                else:
                    count += 1
                    accum[tree.tag].update(result)
        else:
            accum[tree.tag] = tree.text

        return accum

    return internal_iter(element_tree, {})


# красивый вывод в виде JSON
print(
    json.dumps(make_dict_from_tree(
        xml.etree.ElementTree.fromstring(xml_string)),
        indent=1), ',', count)
