import time


def log_time(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time_passed = time.time() - start
        print(f'Czas trwania: {time_passed}')
        return result

    return wrapped


@log_time
def qsort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    lesser = [el for el in data[1:] if el < pivot]
    greater_equal = [el for el in data[1:] if el >= pivot]
    return qsort(lesser) + [pivot] + qsort(greater_equal)


r = qsort([4, 6, 23, 0, 0, 2, -34, 5, 87])
print(r)

# def test_empty():
#     assert qsort([]) == []
#
#
# def test_single_element():
#     assert qsort([3]) == [3]
#
#
# def test_quicksort():
#     assert qsort([4, 3, 3, -34, 5, 2, 5, 1]) == [-34, 1, 2, 3, 3, 4, 5, 5]
