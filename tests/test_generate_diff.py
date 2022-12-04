from gendiff import generate_diff
from gendiff.formaters import plain


def test_generate_diff_stylish_plain():

    expected_result = open('tests/fixtures/result_stylish_plain.txt').read()

    diff_json = generate_diff(
        'tests/fixtures/file1_plain.json', 'tests/fixtures/file2_plain.json')
    assert diff_json == expected_result

    diff_yaml = generate_diff(
        'tests/fixtures/file1_plain.yaml', 'tests/fixtures/file2_plain.yaml')
    assert diff_yaml == expected_result


def test_generate_diff_stylish_recursive():

    expected_result = open('tests/fixtures/result_stylish_recurs.txt').read()

    diff_json = generate_diff(
        'tests/fixtures/file1_recurs.json', 'tests/fixtures/file2_recurs.json')
    assert diff_json == expected_result

    diff_yaml = generate_diff(
        'tests/fixtures/file1_recurs.yaml', 'tests/fixtures/file2_recurs.yaml')
    assert diff_yaml == expected_result


def test_generate_diff_plain():

    expected_result = open('tests/fixtures/result_plain.txt').read()

    diff_json = generate_diff(
        'tests/fixtures/file1_recurs.json',
        'tests/fixtures/file2_recurs.json', plain)
    assert diff_json == expected_result

    diff_yaml = generate_diff(
        'tests/fixtures/file1_recurs.yaml',
        'tests/fixtures/file2_recurs.yaml', plain)
    assert diff_yaml == expected_result
