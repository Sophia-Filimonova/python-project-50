from gendiff.parser import parse_file
from gendiff.formaters import stylish, plain, to_json


def generate_diff_tree(dict1, dict2):
    keys = sorted(list(dict1.keys() | dict2.keys()))
    tree = []
    for key in keys:
        node = {}
        node["key"] = key
        if key not in dict1:
            node["value1"] = dict2[key]
            node["action"] = "added"
        elif key not in dict2:
            node["value1"] = dict1[key]
            node["action"] = "removed"
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                node["action"] = "nested"
                node["children"] = generate_diff_tree(
                    dict1[key], dict2[key])
            elif dict1[key] == dict2[key]:
                node["action"] = "same"
                node["value1"] = dict1[key]
            else:
                node["action"] = "changed"
                node["value1"] = dict1[key]
                node["value2"] = dict2[key]
        tree.append(node)
    return tree


def generate_diff(path_to_file1, path_to_file2, format_name='stylish'):
    dict1 = parse_file(path_to_file1)
    dict2 = parse_file(path_to_file2)
    diff_tree = generate_diff_tree(dict1, dict2)
    format_tree = stylish
    if format_name == 'plain':
        format_tree = plain
    elif format_name == 'json':
        format_tree = to_json
    diff = format_tree(diff_tree)
    return diff
