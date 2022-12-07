from gendiff.parser import get_data
from gendiff.formaters import apply_format


def generate_diff_tree(data1, data2):
    keys = sorted(list(data1.keys() | data2.keys()))
    tree = []
    for key in keys:
        node = {}
        node["key"] = key
        if key not in data1:
            node["value1"] = data2[key]
            node["action"] = "added"
        elif key not in data2:
            node["value1"] = data1[key]
            node["action"] = "removed"
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                node["action"] = "nested"
                node["children"] = generate_diff_tree(
                    data1[key], data2[key])
            elif data1[key] == data2[key]:
                node["action"] = "same"
                node["value1"] = data1[key]
            else:
                node["action"] = "changed"
                node["value1"] = data1[key]
                node["value2"] = data2[key]
        tree.append(node)
    return tree


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    data1 = get_data(path_to_file1)
    data2 = get_data(path_to_file2)
    diff_tree = generate_diff_tree(data1, data2)
    return apply_format(diff_tree, format)
