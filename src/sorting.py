import random
from utils import split_through_pivot, merge_arrays


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def selection_sort(array):
    for i in range(len(array) - 1):
        mi = array[i]
        mi_idx = i
        for j in range(i, len(array)):
            if array[j] < mi:
                mi = array[j]
                mi_idx = j

        array[i], array[mi_idx] = array[mi_idx], array[i]


def merge_sort(array):
    array_length = len(array)
    if array_length < 2:
        return [*array]

    mid_idx = array_length // 2
    left_arr = merge_sort(array[:mid_idx])
    right_arr = merge_sort(array[mid_idx:])

    return merge_arrays(left_arr, right_arr)


def quick_sort(array):
    array_length = len(array)
    if array_length < 2:
        return [*array]

    pivot = random.choice(array)
    less, equal, more = split_through_pivot(array, pivot)

    return [*quick_sort(less), *equal, *quick_sort(more)]
