import math
import random


def swap(data, a, b):
    """Swap the indicies a and b in the array data

    @param data List to swap elements in
    @param a First index to swap
    @param b Second index to swap
    """
    temp = data[a]
    data[a] = data[b]
    data[b] = temp
    return data


def find_pivot(data, left, right):
    """Find a pivot in the dataset between the two given indicies.

    This implementation just uses a random index between two given bounds
    for the pivot.

    @param data The list to find the pivot in
    @param left The lower bound in which to find the pivot
    @param right The upper bound in which to find the pivot
    """
    return int(left + math.floor(random.random() * (right - left + 1)))


def partition(data, left, right, pivot_index):
    """ Parition the data between the bounds given an index to pivot around.

    @param data The list of elements to partition
    @param left The lower bound to partition between
    @param right The upper bound to parition between
    @param pivot_index The index to pivot about
    """
    pivot = data[pivot_index]
    data = swap(data, pivot_index, right)
    store_index = left

    for i in range(left, right):
        if(data[i] <= pivot):
            data = swap(data, i, store_index)
            store_index = store_index + 1

    data = swap(data, store_index, right)
    return store_index
