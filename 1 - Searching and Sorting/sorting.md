## Sorting algorithms  

In computer science, a **sorting algorithm** is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) that require sorted lists to work correctly.  
More formally, the output must satisfy two conditions:  
1. The output is in nondecreasing order (each element is no smaller than the previous element according to the desired total order);  
2. The output is a permutation, or reordering, of the input.  

### Bubble sort  

*Bubble sort* is a simple sorting algorithm. The algorithm starts at the beginning of the data set. It compares the first two elements, and if the first is greater than the second, then it swaps them. It continues doing this for each pair of adjacent elements to the end of the data set.  

The best case for bubble sort occurs when the list is already sorted. In this case, bubble sort makes one pass through the list, performing no swaps and N-1 comparisons.  
The worst case for bubble sort occurs when the list is in reverse order. In this case, every item will have to be swapped with every other item on every pass through the algorithm. There will be **O(n&#x00B2)** comparisons.
