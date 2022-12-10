from gendiff import generate_diff
import pytest
import os.path


@pytest.mark.parametrize("file1, file2, result, format", [(
    'file1_plain.json',
    'file2_plain.json',
    'result_stylish_plain.txt',
    'stylish'), (
    'file1_plain.yaml',
    'file2_plain.yaml',
    'result_stylish_plain.txt',
    'stylish'), (
    'file1_recurs.json',
    'file2_recurs.json',
    'result_stylish_recurs.txt',
    'stylish'), (
    'file1_recurs.yaml',
    'file2_recurs.yaml',
    'result_stylish_recurs.txt',
    'stylish'), (
    'file1_recurs.json',
    'file2_recurs.json',
    'result_plain.txt',
    'plain'), (
    'file1_recurs.yaml',
    'file2_recurs.yaml',
    'result_plain.txt',
    'plain'), (
    'file1_recurs.json',
    'file2_recurs.json',
    'result_to_json.txt',
    'json'), (
    'file1_recurs.yaml',
    'file2_recurs.yaml',
    'result_to_json.txt',
    'json')])
def test_generate_diff(file1, file2, result, format):

    def get_path(file_name):
        return os.path.join('tests/fixtures/', file_name)

    with open(get_path(result)) as f:
        expected_result = f.read()
        diff = generate_diff(get_path(file1), get_path(file2), format)
        assert diff == expected_result
