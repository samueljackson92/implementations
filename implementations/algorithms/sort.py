from _util import *


def quicksort(data, left=None, right=None, pivot_method='simple'):
    """ In place implementation of quicksort.

    @param data The list of elements to sort.
    @param left The lower bound to sort between.
    @param right The upper bound to sort between.
    """
    if left is None and right is None:
        left = 0
        right = len(data)-1

    if left < right:
        pivot_index = find_pivot(data, left, right)
        pivot_index = partition(data, left, right, pivot_index)
        data = quicksort(data, left, pivot_index-1, pivot_method)
        data = quicksort(data, pivot_index+1, right, pivot_method)

    return data


def bubblesort(data):
    """ Implementation of bubble sort.

    @param data The list of elements to sort
    """
    for i in range(len(data)):
        for j in range(len(data)-1):
            if (data[j] > data[j+1]):
                data = swap(data, j, j+1)

    return data


def shakersort(data):
    """ Implementation of shaker sort

    @param data The list of elements to sort
    """
    swapped = True
    n = len(data)
    while swapped:
        swapped = False

        for i in range(0, n-2):
            if (data[i] > data[i+1]):
                data = swap(data, i, i+1)
                swapped = True

        if not swapped:
            break

        swapped = False

        for i in range(n-2, -1, -1):
            if(data[i] > data[i+1]):
                data = swap(data, i, i+1)
                swapped = True

    return data


def selectionsort(data):
    """ Implementation of selection sort

    @param data The list of elements to sort
    """
    for i in range(len(data)-1):
        min_index = i

        for j in range(i+1, len(data)):
            if(data[j] < data[min_index]):
                min_index = j

        if(min_index != i):
            data = swap(data, min_index, i)

    return data


def insertionsort(data):
    """ Implementation of insertion sort

    @param data The list of elements to sort
    """
    for i in range(1, len(data)):
        value_to_insert = data[i]
        hole_index = i

        while hole_index > 0 and value_to_insert < data[hole_index-1]:
            data[hole_index] = data[hole_index-1]
            hole_index = hole_index - 1

        data[hole_index] = value_to_insert

    return data


def generate_gaps():
    """ Gap generator for shell sort

    This yields sucessively smaller gaps to be used in the sorting strategy for
    shell sort. This sequence is taken from Ciura, 2001.
    """
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        yield gap


def shellsort(data):
    """ Implementation of a shell sort

    @param data The list of elements to sort
    """
    n = len(data)
    for gap in generate_gaps():
        for i in xrange(gap, n):
            tmp = data[i]
            j = i
            while (j >= gap and data[j-gap] > tmp):
                data[j] = data[j-gap]
                j -= gap

            data[j] = tmp


def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result += left
            return result
        elif len(right) > 0:
            result += right
            return result

    return result


def mergesort(data):
    if len(data) <= 1:
        return data

    middle = len(data)/2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])

    return merge(left, right)
