import random

arr = [random.randrange(100) for i in range(10)]  # Generate random list


def checkSort(array) -> bool:  # Function for check sort status
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:  # If all elements less than the following then sorted is True
            return True
    return False


def bubble(array):  # Bubble sort function
    done = True
    while done:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Replace element
                break
        done = checkSort(array)  # Check sorted status
    return array


print(arr)
print(bubble(arr))
