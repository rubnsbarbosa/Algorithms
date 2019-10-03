# Input : A collection A = {a1, . . . , an}
# Output: An array A' containing all elements of A in nondecreasing order

A = [2, 4, 1, 6, 5, 3]

def selection_sort(array):
    for i in range(len(array)):
        low = i
        for j in range(i+1, len(array)):
            if array[j] < array[low]:
                low = j
        aux = array[low]
        array[low] = array[i]
        array[i] = aux
    return array

response = selection_sort(A)
print(response)
