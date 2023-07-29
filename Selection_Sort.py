import time
def Selection_Sort(array_element):
    n = len(array_element)
    initial_time = time.perf_counter_ns()
    for i in range(0, n):
        Minimum_value = array_element[i]
        Minimum_index = i
        for j in range(i + 1, n):
            if array_element[j] < Minimum_value:
                Minimum_value = array_element[j]
                Minimum_index = j
        array_element[i], array_element[Minimum_index] = array_element[Minimum_index], array_element[i]
    Final_time = time.perf_counter_ns()
    print(f"Execution time {Final_time - initial_time:0.2f} ns")
    return array_element

array_element = [20, 5, 6000, 8, 10]
Selection_Sort(array_element)
print(f"Sorted array is {array_element}")

