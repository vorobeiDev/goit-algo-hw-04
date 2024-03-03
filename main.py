import timeit
import random
from merge_sort import merge_sort
from insertion_sort import insertion_sort

test_arr = [random.randint(0, 1000) for _ in range(1000)]

merge_sort_time = timeit.timeit('merge_sort(test_arr.copy())', globals=globals(), number=100)

insertion_sort_time = timeit.timeit('insertion_sort(test_arr.copy())', globals=globals(), number=100)

timsort_time = timeit.timeit('sorted(test_arr.copy())', globals=globals(), number=100)

print(f"Merge Sort Time: {merge_sort_time}")
print(f"Insertion Sort Time: {insertion_sort_time}")
print(f"Timsort Time: {timsort_time}")
