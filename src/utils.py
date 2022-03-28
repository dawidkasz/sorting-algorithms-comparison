def split_through_pivot(array, pivot):
    less = []
    equal = []
    more = []

    for el in array:
        if el == pivot:
            equal.append(el)
        elif el < pivot:
            less.append(el)
        else:
            more.append(el)

    return less, equal, more


def merge_arrays(left_arr, right_arr):
    left_length = len(left_arr)
    right_length = len(right_arr)
    idx_in_left = 0
    idx_in_right = 0

    merged_arr = []
    while idx_in_left < left_length or idx_in_right < right_length:
        if idx_in_left == left_length:
            merged_arr.append(right_arr[idx_in_right])
            idx_in_right += 1
        elif idx_in_right == right_length:
            merged_arr.append(left_arr[idx_in_left])
            idx_in_left += 1
        elif left_arr[idx_in_left] < right_arr[idx_in_right]:
            merged_arr.append(left_arr[idx_in_left])
            idx_in_left += 1
        else:
            merged_arr.append(right_arr[idx_in_right])
            idx_in_right += 1

    return merged_arr


def seconds_to_milliseconds(num):
    return num * 10**3
