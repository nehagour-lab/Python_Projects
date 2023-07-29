import time
initial_time = time.perf_counter_ns()
def Merge_sort(array_elements):
    if len(array_elements) > 1:
        median = int(len(array_elements)) / 2
        Left_half_elements = array_elements[:int(median)]  ## 0 to median-1
        Right_half_elements = array_elements[int(median):]  ## median to end element
        Merge_sort(Left_half_elements)
        Merge_sort(Right_half_elements)
        i = j = k = 0
        while i < len(Left_half_elements) and j < len(Right_half_elements):
            if Left_half_elements[i] <= Right_half_elements[j]:
                array_elements[k] = Left_half_elements[i]
                i = i+1
            else:
                array_elements[k] = Right_half_elements[j]
                j = j+1
            k =k+1
        while i < len(Left_half_elements):
            array_elements[k] = Left_half_elements[i]
            i = i+1
            k = k+1
        while j < len(Right_half_elements):
            array_elements[k] = Right_half_elements[j]
            j =j+1
            k =k+1

Final_time = time.perf_counter_ns()
print(f"Execution time {Final_time - initial_time:0.2f} ns")

array_elements = [20, 5, 6000, 8, 10]
Merge_sort(array_elements)
print(f"sorted array is {array_elements}")


