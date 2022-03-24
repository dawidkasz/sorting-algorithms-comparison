from src.utils import get_median_of_three, split_through_pivot, merge_arrays


def bubble_sort(array):
    array_length = len(array)
    if array_length < 2:
        return array

    for i in range(array_length - 1):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


def selection_sort(array):
    array_length = len(array)
    if array_length < 2:
        return array

    for i in range(array_length - 1):
        temp = array[i::]
        min_val = min(temp)
        min_index = temp.index(min_val) + i
        array[i], array[min_index] = array[min_index], array[i]
    return array


def merge_sort(array):
    array_length = len(array)
    if array_length < 2:
        return array

    mid_idx = array_length // 2
    left_arr = merge_sort(array[:mid_idx])
    right_arr = merge_sort(array[mid_idx:])

    return merge_arrays(left_arr, right_arr)


def quick_sort(array):
    array_length = len(array)
    if array_length < 2:
        return array

    pivot = get_median_of_three(array[0], array[array_length // 2], array[-1])
    less, equal, more = split_through_pivot(array, pivot)

    return [*quick_sort(less), *equal, *quick_sort(more)]
