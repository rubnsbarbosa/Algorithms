# Input : A collection A = {a1, . . . , an}
# Output: An array A' containing all elements of A in nondecreasing order

A = [2, 4, 1, 6, 5, 3]

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
    return array

response = bubble_sort(A)
print(response)
