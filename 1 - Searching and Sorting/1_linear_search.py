# Input: A collection of elements A = {a1,...,an} and a key ek
# Output: An element a ∈ A such that a=ek according to some criteria; φ if no such element exists

A = [42, 4, 9, 4, 102, 34, 12, 0]

def linear_search(list_elements, key_element):
    for i in list_elements:
        if i == key_element:
            return i

def linear_search_index(list_elements, key_element):
    for idx in range(len(list_elements)):
        if list_elements[idx] == key_element:
            return idx, list_elements[idx]

response1 = linear_search(A, 4)
print(response1)

response2 = linear_search_index(A, 4)
print(response2)
