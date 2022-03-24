def get_median_of_three(el1, el2, el3):
    max_el = max(el1, el2, el3)

    if max_el == el1:
        return max(el2, el3)
    elif max_el == el2:
        return max(el1, el3)
    else:
        return max(el1, el2)


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
