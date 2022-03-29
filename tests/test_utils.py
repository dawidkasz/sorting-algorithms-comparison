from src import utils
from src.utils import partition, merge_arrays


def test_partition(monkeypatch):
    monkeypatch.setattr(utils.random, 'randint', lambda x, y: 5)

    array = [9, 4, 3, 7, 12, 8, 16, 21, 9, 5, 8]
    expected = [9, 4, 3, 7, 8, 12, 16, 21, 9, 5, 8]

    q = partition(array, 1, 5)

    assert q == 4
    assert array == expected


def test_merge_arrays():
    left_arr = [1, 4, 6, 7, 8, 12, 13]
    right_arr = [2, 3, 4, 20]
    expected = [1, 2, 3, 4, 4, 6, 7, 8, 12, 13, 20]

    assert merge_arrays(left_arr, right_arr) == expected
