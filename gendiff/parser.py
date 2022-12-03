import json
import yaml


def parse_file(path_to_file):
    extension = path_to_file.split('.')[-1]
    if extension == 'json':
        dict = json.load(open(path_to_file))
    if extension in ('yaml', 'yml'):
        dict = yaml.safe_load(open(path_to_file))
    return dict
