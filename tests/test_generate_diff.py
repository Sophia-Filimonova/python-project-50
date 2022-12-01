from gendiff.generate_diff import generate_diff


def test_generate_diff():
    f = open('tests/fixtures/result_json.txt', 'r')
    expected_result = f.read()
    f.close()
    diff = generate_diff(
        'tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert diff == expected_result