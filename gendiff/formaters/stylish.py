def convert(value, indent):
    if value == "no such key":
        return None
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        keys = sorted(list(value.keys()))
        indent += '    '
        lines = ['{']
        for key in keys:
            lines.append(f"{indent}    {key}: {convert(value[key], indent)}")
        lines.append(indent + '}')
        return '\n'.join(lines)
    return str(value).lower()


def stylish(tree, depth=0):   # noqa: C901
    indent = '    ' * depth
    lines = ['{']
    for node in tree:
        key = node["key"]
        value1 = convert(node.get("value1", "no such key"), indent)
        value2 = convert(node.get("value2", "no such key"), indent)
        if node["action"] == "nested":
            lines.append(f'{indent}    {key}: '
                         f'{stylish(node["children"], depth + 1)}')
        elif node["action"] == "added":
            lines.append(f'{indent}  + {key}: {value1}')
        elif node["action"] == "removed":
            lines.append(f'{indent}  - {key}: {value1}')
        elif node["action"] == "same":
            lines.append(f'{indent}    {key}: {value1}')
        elif node["action"] == "changed":
            lines.append(f'{indent}  - {key}: {value1}')
            lines.append(f'{indent}  + {key}: {value2}')
    lines.append(indent + '}')
    return '\n'.join(lines)
