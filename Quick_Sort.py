import time
import random


def partition(array_elements, FIRST_index, LAST_index):
    PARTITION_element_pivot = FIRST_index
    i = FIRST_index
    for j in range(FIRST_index + 1, LAST_index + 1):
        if array_elements[j] <= array_elements[PARTITION_element_pivot]:
            (array_elements[i], array_elements[j]) = (array_elements[j], array_elements[i])
            i = i + 1
    (array_elements[PARTITION_element_pivot], array_elements[i - 1]) = (
    array_elements[i - 1], array_elements[PARTITION_element_pivot])
    PARTITION_element_pivot = i - 1
    return PARTITION_element_pivot


initial_time = time.perf_counter_ns()


def Quick_sort(array_elements, FIRST_index, LAST_index):
    n = len(array_elements)
    if FIRST_index < LAST_index:
        Random_PARTITION_element_pivot = random.randrange(FIRST_index, LAST_index)
        array_elements[FIRST_index], array_elements[Random_PARTITION_element_pivot] = array_elements[
            Random_PARTITION_element_pivot], array_elements[FIRST_index]
        PARTITION_element = partition(array_elements, FIRST_index, LAST_index)
        Quick_sort(array_elements, FIRST_index, PARTITION_element - 1)
        Quick_sort(array_elements, PARTITION_element + 1, LAST_index)


Final_time = time.perf_counter_ns()
print(f"Execution time {Final_time - initial_time:0.2f} ns")

array_elements = [20, 5, 6000, 8, 10]
Quick_sort(array_elements, 0, len(array_elements) - 1)
print(f"Sorted array is{array_elements}")

