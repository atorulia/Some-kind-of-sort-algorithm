# It was hard

import random

arr = [random.randrange(100) for i in range(10)]  # Generate random list


def checkSort(array) -> bool:  # Function for check sort status
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:  # If all elements less than the following then sorted is True
            return True
    return False


def sort(a, b):
    if a > b:
        return b, a
    else:
        return a, b


def sortArr(a, b) -> list:
    array = a + b
    done = True
    while done:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = sort(array[i], array[i + 1])
        done = checkSort(array)
    return array


def merge(array):
    firstArr = [array[i] for i in range(len(array) // 2)]
    secondArr = [array[i] for i in range(len(array) // 2, len(array))]
    if len(firstArr) > 2 or len(secondArr) > 2:
        return sortArr(merge(firstArr), merge(secondArr))
    else:
        return sortArr(firstArr, secondArr)


print(arr)
print(merge(arr))
