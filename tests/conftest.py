import os
import pytest


def pytest_configure():
    pytest.test_case = 'test_case'
    pytest.sorting_test_cases = ['test_case_numbers_1',
                                 'test_case_numbers_2',
                                 'test_case_numbers_negative',
                                 'test_case_words',
                                 'test_case_sorted',
                                 'test_case_reverse_sorted',
                                 'test_case_empty']
    pytest.pan_tadeusz_relative_path = 'data/pan-tadeusz.txt'


@pytest.fixture
def test_case_numbers_1():
    return (
        [9, 7, 2, 4, 11, 7, 1, 4, 5, 14, 8, 154, 21, 33, 2, 18],
        [1, 2, 2, 4, 4, 5, 7, 7, 8, 9, 11, 14, 18, 21, 33, 154]
    )

@pytest.fixture
def test_case_numbers_2():
    return (
        [34, 3, 29, 26, 9, 40, 5, 12, 3, 37, 7, 32, 42, 44, 3, 21, 35, 18, 42, 45],
        [3, 3, 3, 5, 7, 9, 12, 18, 21, 26, 29, 32, 34, 35, 37, 40, 42, 42, 44, 45]
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
def test_case_reverse_sorted():
    return (
        [7, 4, 2, 0, -3],
        [-3, 0, 2, 4, 7]
    )


@pytest.fixture
def test_case_empty():
    return (
        [],
        []
    )


@pytest.fixture(params=[100, *[n for n in range(1000, 11000, 1000)], 20000, 30000])
def pan_tadeusz(request):
    words_array = []
    n_words = request.param

    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             pytest.pan_tadeusz_relative_path)
    with open(file_path) as f_handle:
        for line in f_handle.readlines():
            for word in line.split(' '):
                word = word.strip()
                if not word:
                    continue
                words_array.append(word)

                if len(words_array) >= n_words:
                    return words_array

        return words_array
