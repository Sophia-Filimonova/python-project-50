from gendiff.parser import parse_file
from gendiff.formaters import stylish
# import yaml


def convert(value):
    if isinstance(value, dict):
        keys = sorted(list(value.keys()))
        new_dict = {}
        for key in keys:
            new_dict['     ' + key] = convert(value[key])
        return new_dict
    return value


def generate_diff_dict(dict1, dict2):
    keys = sorted(list(dict1.keys() | dict2.keys()))
    diff_dict = {}
    i = 0
    for key in keys:
        if key not in dict1:
            diff_dict[str(i) + '  + ' + key] = convert(dict2[key])
        elif key not in dict2:
            diff_dict[str(i) + '  - ' + key] = convert(dict1[key])
        else:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff_dict[str(i) + '    ' + key] = generate_diff_dict(
                    dict1[key], dict2[key])
            elif dict1[key] == dict2[key]:
                diff_dict[str(i) + '    ' + key] = convert(dict1[key])
            else:
                diff_dict[str(i) + '  - ' + key] = convert(dict1[key])
                i += 1
                diff_dict[str(i) + '  + ' + key] = convert(dict2[key])
        i += 1
    return diff_dict


def generate_diff(path_to_file1, path_to_file2, format_dict=stylish):
    dict1 = parse_file(path_to_file1)
    dict2 = parse_file(path_to_file2)

    # open('tests/fixtures/file1_recurs.yaml', 'w').write(yaml.dump(dict1))
    # open('tests/fixtures/file2_recurs.yaml', 'w').write(yaml.dump(dict2))

    diff_dict = generate_diff_dict(dict1, dict2)
    diff_string = format_dict(diff_dict)

    return diff_string
