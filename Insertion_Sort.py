import time


def Insertion_sort(array_elements):
    n = len(array_elements)
    initial_time = time.perf_counter_ns()
    for i in range(0, n):
        currentValue = array_elements[i]
        currentIndex = i
        while currentIndex > 0 and array_elements[currentIndex - 1] > currentValue:
            array_elements[currentIndex] = array_elements[currentIndex - 1]
            currentIndex = currentIndex - 1
            array_elements[currentIndex] = currentValue
    final_time = time.perf_counter_ns()
    print(f"Execution time {final_time - initial_time:0.2f} ns")
    return array_elements


array_elements = [20, 5, 6000, 8, 10]
Insertion_sort(array_elements)
print(f"Sorted array is {array_elements}")


