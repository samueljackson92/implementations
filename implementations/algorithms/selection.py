from _util import *


def quick_select(data, left=None, right=None, k=0):
    """ Implementation of the quick select algorithm

    This acts as a one armed quick sort to find the kth smallest item in an
    unsorted list. This algorithm performed in-place and will paritally sort
    the data.

    @param data The list of elements to sort.
    @param left The lower bound to sort between.
    @param right The upper bound to sort between.
    @param k We wish to find the kth smallest number
    """
    if left is None and right is None:
        left = 0
        right = len(data)-1

    if left == right:
        return data[left]

    pivot_index = find_pivot(data, left, right)
    pivot_index = partition(data, left, right, pivot_index)

    if k == pivot_index:
        return data[pivot_index]
    elif k < pivot_index:
        return quick_select(data, left, pivot_index-1, k)
    else:
        return quick_select(data, pivot_index+1, right, k)