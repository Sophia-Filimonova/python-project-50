import json
import yaml


def parse_file(path_to_file):
    parts = path_to_file.split('.')
    if parts[-1] == 'json':
        dict = json.load(open(path_to_file))
    if parts[-1] in ('yaml', 'yml'):
        dict = yaml.safe_load(open(path_to_file))
    return dict
