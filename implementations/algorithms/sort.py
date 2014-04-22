
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
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


def mergesort(data):
    if len(data) <= 1:
        return data

    middle = len(data)/2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])

    return merge(left, right)
