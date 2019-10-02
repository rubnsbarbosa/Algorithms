# Input: A sorted collection of elements A = {a1,...,an} and a key ek
# Output: An element a ∈ A such that a = ek according to some criteria; φ if no such element exists

arr = [6, 5, 4, 3, 2, 1]
def ascending_order(array):
    for i in range(len(array)):
        a = i + 1
        for j in range(a, len(array)):
            if array[i] > array[j]:
                aux = array[j]
                array[j] = array[i]
                array[i] = aux

def show_array(array):
    for i in range(len(array)):
        print('Index: {} - Value: {}'.format(i, array[i]))

def binary_search(array, key_element):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        middle_index = int((left_index + right_index) / 2)

        if key_element == array[middle_index]:
            return middle_index, array[middle_index]

        elif key_element < array[middle_index]:
            right_index = middle_index - 1

        else:
            left_index = middle_index + 1


ascending_order(arr)
show_array(arr)
resp = binary_search(arr, 2)
print('Index and Value', resp)
