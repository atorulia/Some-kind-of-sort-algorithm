import random

arr = [random.randrange(100) for i in range(10)]  # Creat random list


def checkSort(array) -> bool:  # Function for check sort status
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:  # If all elements less than the following then sorted is True
            return True
    return False


def randomQuick(array):  # Random quick sort function
    done = True
    while done:
        for i in range(len(array) - 1):
            point = random.randrange(len(array) - 1)  # Creat random point from start
            if array[point] > array[point + 1]:
                sortPoint = array[point]
                if array[point + 1] < sortPoint:
                    array[point], array[point + 1] = array[point + 1], array[point]  # Replace elements
                    break
        done = checkSort(array)  # Check sort status
    return array


print(arr)
print(randomQuick(arr))



