import json
import yaml


def parse_file(content, format_name):
    if format_name == 'json':
        return json.load(content)
    if format_name in ('yaml', 'yml'):
        return yaml.safe_load(content)
    raise Exception('Invalid type of file')


def get_data(path_to_file):
    format_name = path_to_file.split('.')[-1]
    with open(path_to_file) as file:
        return parse_file(file, format_name)
