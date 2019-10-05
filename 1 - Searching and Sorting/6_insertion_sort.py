# Input : A collection A = {a1, . . . , an}
# Output: An array A' containing all elements of A in nondecreasing order

A = [2, 4, 1, 6, 5, 3]

def insertion_sort(array):
    for i in range(0, len(array)):
        aux = array[i]
        j = i
        while(j > 0 and array[j-1] > aux):
            array[j] = array[j-1]
            j = j - 1
        array[j] = aux
    return array

response = insertion_sort(A)
print(response)
