def stringify(value):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    return str(value).lower()


def stylish(diff_dict):

    def iter_(dict_, depth):
        keys = list(dict_.keys())
        indent = '    ' * depth
        result = ['{']
        for key in keys:
            value = dict_[key]
            if not isinstance(value, dict):
                result.append(f'{indent}{key}: {stringify(value)}')
            else:
                result.append(f'{indent}{key}: {iter_(value, depth + 1)}')
        result.append(indent + '}')
        result_str = '\n'.join(result)
        return result_str

    return iter_(diff_dict, 0)
