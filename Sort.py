# Methods    Aver.      Best       Worst        Space      Stability
# Bubble    O(n^2)      O(n)       O(n^2)        O(1)	      Yes
# Select    O(n^2)     O(n^2)      O(n^2)        O(1)	      Yes
# Insert    O(n^2)      O(n)       O(n^2)        O(1)	      Yes
# Heap     O(nlogn)   O(nlogn)    O(nlogn)       O(1)         No
# Merge    O(nlogn)   O(nlogn)    O(nlogn)       O(n)	      Yes
# Quick    O(nlogn)   O(nlogn)     O(n^2)      O(logn)~O(n)   No


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


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


nums = [10, 5, 2, 3, 1, 4, 9, 8, 6, 7]
print("Bubble: ", bubbleSort(nums))
print("Select: ", selectSort(nums))
print("Quick: ", quickSort(nums))
