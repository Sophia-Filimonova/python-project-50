def stringify(value):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, list) or isinstance(value, dict):
        return '[complex value]'
    return str(value).lower()


def plain(diff_dict):   # noqa: C901

    def iter_(dict_, path):
        keys = list(dict_.keys())
        result = []
        i = 0
        while i < len(keys):
            key = keys[i][4:]
            value = dict_[keys[i]]
            path.append(key)
            sign = keys[i][2]
            if sign == '+':
                result.append(
                    f"Property '{'.'.join(path)}' was added "
                    f"with value: {stringify(value)}")
            elif sign == '-':
                if i < len(keys) - 1:
                    next_key = keys[i + 1][4:]
                    next_value = dict_[keys[i + 1]]
                else:
                    next_key = None
                    next_value = None
                if key == next_key:
                    result.append(
                        f"Property '{'.'.join(path)}' was updated. "
                        f"From {stringify(value)} to {stringify(next_value)}")
                    i += 1
                else:
                    result.append(f"Property '{'.'.join(path)}' was removed")
            elif sign == ' ':
                if isinstance(value, dict):
                    result.append(iter_(value, path))
            i += 1
            path.pop()
        result_str = '\n'.join(result)
        return result_str

    return iter_(diff_dict, [])
