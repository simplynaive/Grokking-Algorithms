# Methods    Aver.      Best       Worst        Space      Stability
# Bubble    O(n^2)      O(n)       O(n^2)        O(1)	      Yes
# Select    O(n^2)     O(n^2)      O(n^2)        O(1)	      Yes
# Insert    O(n^2)      O(n)       O(n^2)        O(1)	      Yes
# Heap     O(nlogn)   O(nlogn)    O(nlogn)       O(1)         No
# Merge    O(nlogn)   O(nlogn)    O(nlogn)       O(n)	      Yes
# Quick    O(nlogn)   O(nlogn)     O(n^2)      O(logn)~O(n)   No
import copy


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def selectSort(array):
    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            min = j if array[min] > array[j] else min
        if min != i:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp
    return array


def insertSort(array):
    for i in range(len(array)):
        index = array[i]
        j = i
        while j > 0 and array[j - 1] > index:
            array[j] = array[j - 1]
            j -= 1
        array[j] = index
    return array


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


nums = [10, 5, 2, 3, 1, 4, 9, 8, 6, 7]
print("Bubble: ", bubbleSort(copy.deepcopy(nums)))
print("Select: ", selectSort(copy.deepcopy(nums)))
print("Insert: ", insertSort(copy.deepcopy(nums)))
print("Quick: ", quickSort(copy.deepcopy(nums)))
