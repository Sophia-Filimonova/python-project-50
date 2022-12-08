def stringify(value):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, list) or isinstance(value, dict):
        return '[complex value]'
    return str(value).lower()


def plain(tree, path=[]):
    lines = []
    for node in tree:
        path.append(node["key"])
        full_path = '.'.join(path)
        if node["action"] == "added":
            lines.append(
                f"Property '{full_path}' was added "
                f'with value: {stringify(node["value1"])}')
        elif node["action"] == "removed":
            lines.append(
                f"Property '{full_path}' was removed")
        elif node["action"] == "changed":
            lines.append(
                f"Property '{full_path}' was updated. "
                f'From {stringify(node["value1"])} '
                f'to {stringify(node["value2"])}')
        elif node["action"] == "nested":
            lines.append(plain(node["children"], path))
        path.pop()
    output = '\n'.join(lines)
    return output
