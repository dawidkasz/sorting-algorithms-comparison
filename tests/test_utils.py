from src.utils import get_median_of_three, split_through_pivot


def test_get_median_of_three_first_largest():
    assert get_median_of_three(10, 8, -5) == 8


def test_get_median_of_three_second_largest():
    assert get_median_of_three('a', 'f', 'd') == 'd'


def test_get_median_of_three_third_largest():
    assert get_median_of_three(123, 12, 1234) == 123


def test_split_through_pivot():
    array = [9, 4, 3, 7, 12, 8, 16, 21, 9, 5, 8]
    expected = ([4, 3, 7, 5], [8, 8], [9, 12, 16, 21, 9])

    assert(split_through_pivot(array, 8)) == expected
