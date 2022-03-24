import os
import pytest


def pytest_configure():
    pytest.test_case = 'test_case'
    pytest.sorting_test_cases = ['test_case_numbers',
                                 'test_case_numbers_negative',
                                 'test_case_words',
                                 'test_case_sorted',
                                 'test_case_empty']
    pytest.pan_tadeusz_relative_path = 'data/pan-tadeusz.txt'


@pytest.fixture
def test_case_numbers():
    return (
        [9, 7, 2, 4, 11, 7, 1, 4, 5, 14, 8, 154, 21, 33, 2, 18],
        [1, 2, 2, 4, 4, 5, 7, 7, 8, 9, 11, 14, 18, 21, 33, 154]
    )


@pytest.fixture
def test_case_numbers_negative():
    return (
        [-16, -24, 1, 0, 154, 11, 2, -198, 1234, -1234, 12, -8, -16, -16, 5],
        [-1234, -198, -24, -16, -16, -16, -8, 0, 1, 2, 5, 11, 12, 154, 1234]
    )


@pytest.fixture
def test_case_words():
    return (
        ['a', 'ef', 'qwerty', 'eah', 'foo', 'bar', 'foa', 'abc', 'abd'],
        ['a', 'abc', 'abd', 'bar', 'eah', 'ef', 'foa', 'foo', 'qwerty']
    )


@pytest.fixture
def test_case_sorted():
    return (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    )


@pytest.fixture
def test_case_empty():
    return (
        [],
        []
    )


@pytest.fixture(params=[n for n in range(1000, 11000, 1000)])
def pan_tadeusz(request):
    words_array = []
    n_words = request.param

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             pytest.pan_tadeusz_relative_path)
    with open(file_path) as f_handle:
        for word in f_handle.read().split(' ')[:n_words]:
            words_array.append(word.strip())

        return words_array
