import pytest
from src.sorting import bubble_sort, selection_sort, merge_sort, quick_sort


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_bubble_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert bubble_sort(data) == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_selection_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert selection_sort(data) == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_merge_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert merge_sort(data) == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_quick_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert quick_sort(data) == expected


def test_bubble_sort_benchmark(pan_tadeusz, benchmark):
    if len(pan_tadeusz) <= 10000:
        benchmark.extra_info['name'] = 'bubble_sort'
        benchmark.extra_info['sample_size'] = len(pan_tadeusz)
        benchmark(bubble_sort, pan_tadeusz)


def test_selection_sort_benchmark(pan_tadeusz, benchmark):
    if len(pan_tadeusz) <= 10000:
        benchmark.extra_info['name'] = 'selection_sort'
        benchmark.extra_info['sample_size'] = len(pan_tadeusz)
        benchmark(selection_sort, pan_tadeusz)


def test_merge_sort_benchmark(pan_tadeusz, benchmark):
    benchmark.extra_info['name'] = 'merge_sort'
    benchmark.extra_info['sample_size'] = len(pan_tadeusz)
    benchmark(merge_sort, pan_tadeusz)


def test_quick_sort_benchmark(pan_tadeusz, benchmark):
    benchmark.extra_info['name'] = 'quick_sort'
    benchmark.extra_info['sample_size'] = len(pan_tadeusz)
    benchmark(quick_sort, pan_tadeusz)
