import time


def Bubble_sort(array_elements):
    n = len(array_elements)
    initial_time = time.perf_counter_ns()
    for i in range(0, n):
        for j in range(n - 1):
            if array_elements[j] > array_elements[j + 1]:
                array_elements[j], array_elements[j + 1] = array_elements[j + 1], array_elements[j]
    final_time = time.perf_counter_ns()
    print(f"Execution time {final_time - initial_time:0.2f} ns")
    return array_elements


array_elements = [20, 5, 6000, 8, 10]
Bubble_sort(array_elements)
print(f"Sorted array is {array_elements}")

