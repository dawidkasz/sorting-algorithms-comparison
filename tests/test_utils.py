from src.utils import split_through_pivot, merge_arrays


def test_split_through_pivot():
    array = [9, 4, 3, 7, 12, 8, 16, 21, 9, 5, 8]
    expected = ([4, 3, 7, 5], [8, 8], [9, 12, 16, 21, 9])

    assert(split_through_pivot(array, 8)) == expected


def test_merge_arrays():
    left_arr = [1, 4, 6, 7, 8, 12, 13]
    right_arr = [2, 3, 4, 20]
    expected = [1, 2, 3, 4, 4, 6, 7, 8, 12, 13, 20]

    assert merge_arrays(left_arr, right_arr) == expected
