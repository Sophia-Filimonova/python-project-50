def stringify(value, indent):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        keys = sorted(list(value.keys()))
        indent += '    '
        lines = ['{']
        for key in keys:
            lines.append(f"{indent}    {key}: {stringify(value[key], indent)}")
        lines.append(indent + '}')
        return '\n'.join(lines)
    return str(value).lower()


def stylish(diff_tree):

    def iter_(tree, depth=0):
        indent = '    ' * depth
        lines = ['{']
        for node in tree:
            if node["action"] == "added":
                lines.append(
                    f'{indent}  + {node["key"]}: '
                    f'{stringify(node["value1"], indent)}')
            elif node["action"] == "removed":
                lines.append(
                    f'{indent}  - {node["key"]}: '
                    f'{stringify(node["value1"], indent)}')
            elif node["action"] == "same":
                lines.append(
                    f'{indent}    {node["key"]}: '
                    f'{stringify(node["value1"], indent)}')
            elif node["action"] == "changed":
                lines.append(
                    f'{indent}  - {node["key"]}: '
                    f'{stringify(node["value1"], indent)}')
                lines.append(
                    f'{indent}  + {node["key"]}: '
                    f'{stringify(node["value2"], indent)}')
            elif node["action"] == "nested":
                lines.append(
                    f'{indent}    {node["key"]}: '
                    f'{iter_(node["children"], depth + 1)}')
        lines.append(indent + '}')
        output = '\n'.join(lines)
        return output

    return iter_(diff_tree)
