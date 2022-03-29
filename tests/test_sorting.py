import pytest
from src.sorting import bubble_sort, selection_sort, merge_sort, quick_sort, insertion_sort


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
def test_insertion_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    insertion_sort(data)
    assert data == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_merge_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    assert merge_sort(data) == expected


@pytest.mark.parametrize(pytest.test_case, pytest.sorting_test_cases)
def test_quick_sort(test_case, request):
    data, expected = request.getfixturevalue(test_case)
    quick_sort(data)
    assert data == expected


def test_bubble_sort_benchmark(data, benchmark):
    def setup():
        return ([data.copy()]), {}

    benchmark.extra_info['name'] = 'bubble_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark.pedantic(bubble_sort, setup=setup, rounds=3, warmup_rounds=1)


def test_selection_sort_benchmark(data, benchmark):
    def setup():
        return ([data.copy()]), {}

    benchmark.extra_info['name'] = 'selection_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark.pedantic(selection_sort, setup=setup, rounds=3, warmup_rounds=1)


def test_insertion_sort_benchmark(data, benchmark):
    def setup():
        return ([data.copy()]), {}
    benchmark.extra_info['name'] = 'insertion_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark.pedantic(insertion_sort, setup=setup, rounds=3, warmup_rounds=1)


def test_merge_sort_benchmark(data, benchmark):
    def setup():
        return ([data.copy()]), {}
    benchmark.extra_info['name'] = 'merge_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark.pedantic(merge_sort, setup=setup, rounds=3, warmup_rounds=1)


def test_quick_sort_benchmark(data, benchmark):
    def setup():
        return ([data.copy()]), {}
    benchmark.extra_info['name'] = 'quick_sort'
    benchmark.extra_info['sample_size'] = len(data)
    benchmark.pedantic(quick_sort, setup=setup, rounds=3, warmup_rounds=1)
