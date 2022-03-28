import pytest
from src.sorting import bubble_sort, selection_sort, merge_sort, quick_sort


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_bubble_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    bubble_sort(data)
    assert data == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_selection_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    selection_sort(data)
    assert data == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_merge_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert merge_sort(data) == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_quick_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert quick_sort(data) == expected


def test_bubble_sort_benchmark(data, benchmark):
    if len(data) <= 10000:
        benchmark.extra_info['name'] = 'bubble_sort'
        benchmark.extra_info['sample_size'] = len(data)
        benchmark(bubble_sort, data)


def test_selection_sort_benchmark(data, benchmark):
    if len(data) <= 10000:
        benchmark.extra_info['name'] = 'selection_sort'
        benchmark.extra_info['sample_size'] = len(data)
        benchmark(selection_sort, data)


def test_merge_sort_benchmark(data, benchmark):
    benchmark.extra_info['name'] = 'merge_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark(merge_sort, data)


def test_quick_sort_benchmark(data, benchmark):
    benchmark.extra_info['name'] = 'quick_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark(quick_sort, data)
