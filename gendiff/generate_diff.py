import json


def generate_diff(path_to_file1, path_to_file2):
    dict1 = json.load(open(path_to_file1))
    dict2 = json.load(open(path_to_file2))
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys = keys1 + keys2
    keys.sort()
    i = 0
    result = ['{']
    while i < len(keys):
        c_key = keys[i]
        if i < len(keys) - 1:
            n_key = keys[i + 1]
        else:
            n_key = None
        if c_key == n_key:
            value1 = dict1[c_key]
            value2 = dict2[c_key]
            if value1 == value2:
                result.append(f'    {c_key}: {str(value1).lower()}')
            else:
                result.append(f'  - {c_key}: {str(value1).lower()}')
                result.append(f'  + {c_key}: {str(value2).lower()}')
            i += 2
        else:
            if c_key in keys1:
                value = dict1[c_key]
                result.append(f'  - {c_key}: {str(value).lower()}')
            else:
                value = dict2[c_key]
                result.append(f'  + {c_key}: {str(value).lower()}')
            i += 1
    result.append('}')
    diff_string = '\n'.join(result)

    return diff_string
