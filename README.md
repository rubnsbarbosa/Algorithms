# Algorithms

Some of the best known algorithms in computer science. :computer:  

## Searching and Sorting Algorithm Analysis

### Searching algorithms

* Linear Search  

```python
def linear_search(list_elements, key_element):
    for i in list_elements:
        if i == key_element:
            return i
```

> Complexity of Linear Search is linear.  
> Best case: **O(1)**  
> Worst case: **O(n)**

___

* Binary Search  

> Iterative  

```python
def binary_search(array, key_element):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle_index = int((low + high) / 2)

        if key_element == array[middle_index]:
            return middle_index, array[middle_index]

        elif key_element < array[middle_index]:
            high = middle_index - 1

        else:
            low = middle_index + 1
```

> Recursive  

```python
def binary_search(array, low, high, key_element):
    if low > high:
        return None
    middle_index = int((low + high) / 2)

    if key_element == array[middle_index]:
        return middle_index, array[middle_index]
    elif array[middle_index] < key_element:
        return binary_search(array, middle_index + 1, high, key_element)
    elif array[middle_index] > key_element:
        return binary_search(array, low, middle_index - 1, key_element)
```

> Complexity of Binary Search is log n.  
> Best case: **O(1)**  
> Worst case: **O(log n)**

### Sorting algorithms

* Bubble Sort  

```python
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
    return array
```

> Complexity of Bubble Sort is **O(n²)**

___

* Selection Sort  

```python
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
```

> Complexity of Selection Sort is **O(n²)**
