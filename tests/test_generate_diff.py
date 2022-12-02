from gendiff import generate_diff


def test_generate_diff():

    expected_result = open('tests/fixtures/result_plain.txt').read()

    diff_json = generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff_json == expected_result

    diff_yaml = generate_diff(
        'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert diff_yaml == expected_result
