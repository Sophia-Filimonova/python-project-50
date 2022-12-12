from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.to_json import to_json


def apply_format(diff_tree, format):
    if format == 'stylish':
        format_tree = stylish
    elif format == 'plain':
        format_tree = plain
    elif format == 'json':
        format_tree = to_json
    else:
        raise Exception('Invalid type of format')
    diff = format_tree(diff_tree)
    return diff
