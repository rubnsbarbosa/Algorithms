# Input : A collection A = {a1, . . . , an}, indices l, r
# Output: An array A' containing all elements of A in nondecreasing order

A = [2, 4, 1, 6, 5, 3]

def quick_sort(array, left, right):
    index = partition(array, left, right)
    if left < index - 1:
        quick_sort(array, left, index - 1)
    if index < right:
        quick_sort(array, index, right)
    return array

def partition(array, i, j):
    a = int( (i + j) / 2)
    pivot = array[a]

    while i <= j:
        while array[i] < pivot:
            i = i + 1
        while array[j] > pivot:
            j = j - 1
        if i <= j:
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
            i = i + 1
            j = j - 1
    return i

response = quick_sort(A, 0, 5)
print(response)
