import random

arr = [random.randrange(100) for i in range(10)]  # Generate random list


def checkSort(array) -> bool:  # Function for check sort status
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:  # If all elements less than the following then sorted is True
            return True
    return False


def selection(array):  # Selection sort function
    for i in range(len(array)):
        min_element = i  # Find min element
        for j in range(i + 1, len(array)):
            if array[min_element] > array[j]:  # Find new min element
                min_element = j
        array[i], array[min_element] = array[min_element], array[i]  # Replace elements
    return array


print(arr)
print(selection(arr))
