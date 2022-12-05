from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file1, file2, result, format", [(
    'tests/fixtures/file1_plain.json',
    'tests/fixtures/file2_plain.json',
    'tests/fixtures/result_stylish_plain.txt',
    'stylish'), (
    'tests/fixtures/file1_plain.yaml',
    'tests/fixtures/file2_plain.yaml',
    'tests/fixtures/result_stylish_plain.txt',
    'stylish'), (
    'tests/fixtures/file1_recurs.json',
    'tests/fixtures/file2_recurs.json',
    'tests/fixtures/result_stylish_recurs.txt',
    'stylish'), (
    'tests/fixtures/file1_recurs.yaml',
    'tests/fixtures/file2_recurs.yaml',
    'tests/fixtures/result_stylish_recurs.txt',
    'stylish'), (
    'tests/fixtures/file1_recurs.json',
    'tests/fixtures/file2_recurs.json',
    'tests/fixtures/result_plain.txt',
    'plain'), (
    'tests/fixtures/file1_recurs.yaml',
    'tests/fixtures/file2_recurs.yaml',
    'tests/fixtures/result_plain.txt',
    'plain'), (
    'tests/fixtures/file1_recurs.json',
    'tests/fixtures/file2_recurs.json',
    'tests/fixtures/result_to_json.txt',
    'json'), (
    'tests/fixtures/file1_recurs.yaml',
    'tests/fixtures/file2_recurs.yaml',
    'tests/fixtures/result_to_json.txt',
    'json')])
def test_generate_diff_stylish_plain(file1, file2, result, format):

    expected_result = open(result).read()
    diff = generate_diff(file1, file2, format)

    assert diff == expected_result
