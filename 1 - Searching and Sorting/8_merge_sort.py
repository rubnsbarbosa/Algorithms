#Input : An array, sub-indices 1 ≤ l, r ≤ n
#Output: An array A' such that A[l, . . . , r] is sorted

A = [2, 4, 1, 6, 5, 3]

def merge_sort(array, left, right):
    middle = int( (low + high) / 2)

    if left < right:
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)
