import random


def partition(array, p, r):
    pv = random.randint(p, r)
    array[pv], array[r] = array[r], array[pv]

    x = array[r]
    i = p
    for j in range(p, r):
        if array[j] <= x:
            array[j], array[i] = array[i], array[j]
            i += 1

    array[i], array[r] = array[r], array[i]

    return i


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
