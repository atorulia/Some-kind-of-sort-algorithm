import random

arr = [random.randrange(100) for i in range(10)]   # Generate random list


def checkSort(array) -> bool:  # Function for check sort status
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:  # If all elements less than the following then sorted is True
            return True
    return False


def insertion(array):  # Insertion sort function
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


print(arr)
print(insertion(arr))
