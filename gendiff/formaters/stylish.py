def convert_to_str(value, indent):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        keys = value.keys()
        indent += '    '
        lines = ['{']
        for key in keys:
            lines.append(f"{indent}    {key}: "
                         f"{convert_to_str(value[key], indent)}")
        lines.append(indent + '}')
        return '\n'.join(lines)
    return str(value).lower()


def stylish(tree, depth=0):    # noqa: C901
    indent = '    ' * depth
    lines = ['{']
    for node in tree:
        key = node["key"]
        value1 = convert_to_str(node.get("value1"), indent)
        value2 = convert_to_str(node.get("value2"), indent)
        if node["action"] == "nested":
            lines.append(f'{indent}    {key}: '
                         f'{stylish(node["children"], depth + 1)}')
            continue
        if node["action"] == "added":
            lines.append(f'{indent}  + {key}: {value1}')
            continue
        if node["action"] == "removed":
            lines.append(f'{indent}  - {key}: {value1}')
            continue
        if node["action"] == "same":
            lines.append(f'{indent}    {key}: {value1}')
            continue
        if node["action"] == "changed":
            lines.append(f'{indent}  - {key}: {value1}')
            lines.append(f'{indent}  + {key}: {value2}')
    lines.append(indent + '}')
    return '\n'.join(lines)
