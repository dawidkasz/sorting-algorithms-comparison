from src.utils import get_median_of_three, split_through_pivot


def bubble_sort(array):
    pass


def selection_sort(array):
    pass


def merge_sort(array):
    pass


def quick_sort(array):
    array_length = len(array)
    if array_length < 2:
        return array

    pivot = get_median_of_three(array[0], array[array_length // 2], array[-1])
    less, equal, more = split_through_pivot(array, pivot)

    return [*quick_sort(less), *equal, *quick_sort(more)]
