import json
import yaml


def parse(file, extension):
    if extension == 'json':
        dict = json.load(file)
    if extension in ('yaml', 'yml'):
        dict = yaml.safe_load(file)
    return dict


def parse_file(path_to_file):
    extension = path_to_file.split('.')[-1]
    file = open(path_to_file)
    return parse(file, extension)
