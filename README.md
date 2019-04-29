# Some-kind-of-sort-algorithm

I have written several interpretations of the most popular sorting algorithms in Python.

# Bubble sort

Bubble sorting or sorting by simple exchanges is one of the simplest sorting algorithms. It is applied
for organizing arrays of small sizes.
The essence of the algorithm is that several passes through the array are performed. With each pass, two adjacent elements are compared in pairs. If they are in the right order, then nothing happens, otherwise they switch places. As a result of the first pass, the maximum element will be at the end, that is, it will pop up like a bubble. Then everything repeats until the entire array is sorted.

# Quick sort

Quick sorting is generally one of the fastest array sorting algorithms, but in practice it is most often used with various modifications. It exemplifies the divide and conquer principle.
The idea of the algorithm is that a support element is selected, relative to which the sorting will take place. Equal and large elements are placed on the right, the smaller - on the left. Then, the first two points are recursively applied to the received subarrays.

# Random quick sort

Random quick sorting is the same as quick sorting, with the only difference that the supporting element is chosen randomly.

# Merge sort

Merge sorting is an algorithm that sorts such data structures where elements are accessed sequentially. This sorting is as follows:
the array is divided into two approximately equal parts, then each of them is sorted. After that, the two sorted sub-arrays merge into one. For this, the first two elements in each of them are compared and, depending on the sorting order, are put in the correct sequence. If one subarray ends, the remaining elements of the second are written after the last element of the first.

# Selection sort

Sorting by selection - here to sort the array, find the element with the minimum value, then compare it with the value of the first unsorted position. If this element is smaller, it becomes a new minimum and their positions change.

# Insertion sort

Sorting inserts - sorting, in which elements are viewed one by one and put in place in accordance with an already ordered array.
