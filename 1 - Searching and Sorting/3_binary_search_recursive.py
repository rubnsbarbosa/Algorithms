arr = [1, 2, 3, 4, 5, 6]

def binary_search(array, low, high, key_element):
    pass
    if low > high:
        return None

    middle_index = int((low + high) / 2)

    if key_element == array[middle_index]:
        return middle_index, array[middle_index] # return index and value
    elif array[middle_index] < key_element:
        return binary_search(array, middle_index + 1, high, key_element)
    elif array[middle_index] > key_element:
        return binary_search(array, low, middle_index - 1, key_element)

# the last parameth is element that I want find
resp = binary_search(arr, 0, 6, 4)
print('Index and Value', resp)
