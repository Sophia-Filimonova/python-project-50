from gendiff.parser import parse_file
from gendiff.formaters import stylish
from gendiff.formaters import plain      # noqa: F401
from gendiff.formaters import to_json    # noqa: F401
# import yaml


def convert(value):
    if isinstance(value, dict):
        keys = sorted(list(value.keys()))
        new_dict = {}
        for key in keys:
            new_dict['    ' + key] = convert(value[key])
        return new_dict
    return value


def generate_diff_dict(dict1, dict2):
    keys = sorted(list(dict1.keys() | dict2.keys()))
    diff_dict = {}
    for key in keys:
        if key not in dict1:
            diff_dict['  + ' + key] = convert(dict2[key])
        elif key not in dict2:
            diff_dict['  - ' + key] = convert(dict1[key])
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff_dict['    ' + key] = generate_diff_dict(
                    dict1[key], dict2[key])
            elif dict1[key] == dict2[key]:
                diff_dict['    ' + key] = convert(dict1[key])
            else:
                diff_dict['  - ' + key] = convert(dict1[key])
                diff_dict['  + ' + key] = convert(dict2[key])
    return diff_dict


def generate_diff(path_to_file1, path_to_file2, format_dict=stylish):
    dict1 = parse_file(path_to_file1)
    dict2 = parse_file(path_to_file2)

    # open('tests/fixtures/file1_recurs.yaml', 'w').write(yaml.dump(dict1))
    # open('tests/fixtures/file2_recurs.yaml', 'w').write(yaml.dump(dict2))

    diff_dict = generate_diff_dict(dict1, dict2)
    diff_string = format_dict(diff_dict)

    return diff_string
