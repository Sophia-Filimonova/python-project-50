from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.to_json import to_json


def apply_format(diff_tree, format):
    if format == 'stylish':
        return stylish(diff_tree)
    elif format == 'plain':
        return plain(diff_tree)
    elif format == 'json':
        return to_json(diff_tree)
    else:
        raise Exception('Invalid type of format')
