
def _swap(data, a, b):
    """Swap the indicies a and b in the array data

    @param data List to swap elements in
    @param a First index to swap
    @param b Second index to swap
    """
    temp = data[a]
    data[a] = data[b]
    data[b] = temp
    return data


def _find_pivot(data, left, right):
    """Find a pivot in the dataset between the two given indicies.

    @param data The list to find the pivot in
    @param left The lower bound in which to find the pivot
    @param right The upper bound in which to find the pivot
    """
    centre = ((right-left)/2) + left
    return centre


def _partition(data, left, right, pivot_index):
    """ Parition the data between the bounds given an index to pivot around.

    @param data The list of elements to partition
    @param left The lower bound to partition between
    @param right The upper bound to parition between
    @param pivotIndex The index to pivot about
    """
    pivot = data[pivot_index]
    data = _swap(data, pivot_index, right)
    storeIndex = left

    for i in range(left, right):
        if(data[i] <= pivot):
            data = _swap(data, i, storeIndex)
            storeIndex = storeIndex + 1

    data = _swap(data, storeIndex, right)
    return storeIndex


def quicksort(data, left=None, right=None):
    """ In place implementation of quicksort.

    @param data The list of elements to sort.
    @param left The lower bound to sort between.
    @param right The upper bound to sort between.
    """
    if left is None and right is None:
        left = 0
        right = len(data)-1

    if left < right:
        pivotIndex = _find_pivot(data, left, right)
        pivotIndex = _partition(data, left, right, pivotIndex)
        data = quicksort(data, left, pivotIndex-1)
        data = quicksort(data, pivotIndex+1, right)

    return data


def bubblesort(data):
    """ Implementation of bubble sort.

    @param data The list of elements to sort
    """
    for i in range(len(data)):
        for j in range(len(data)-1):
            if (data[j] > data[j+1]):
                data = _swap(data, j, j+1)

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
                data = _swap(data, i, i+1)
                swapped = True

        if not swapped:
            break

        swapped = False

        for i in range(n-2, -1, -1):
            if(data[i] > data[i+1]):
                data = _swap(data, i, i+1)
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
            data = _swap(data, min_index, i)

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
