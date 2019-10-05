## Sorting algorithms  

In computer science, a **sorting algorithm** is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) that require sorted lists to work correctly.  
More formally, the output must satisfy two conditions:  
1. The output is in nondecreasing order (each element is no smaller than the previous element according to the desired total order);  
2. The output is a permutation, or reordering, of the input.  

### Bubble sort  

*Bubble sort* is a simple sorting algorithm. The algorithm starts at the beginning of the data set. It compares the first two elements, and if the first is greater than the second, then it swaps them. It continues doing this for each pair of adjacent elements to the end of the data set.  

The best case for bubble sort occurs when the list is already sorted. In this case, bubble sort makes one pass through the list, performing no swaps and N-1 comparisons.  
The worst case for bubble sort occurs when the list is in reverse order. In this case, every item will have to be swapped with every other item on every pass through the algorithm. There will be **O(n²)** comparisons.

### Selection sort

The idea behind *selection sort* is that we put a list in order by placing each item in turn. In other words, we put the smallest item at the start of the list, then the next smallest item at the second position in the list, and so on until the list is in order.  

The best case for selection sort occurs when the list is already sorted. In this case, the number of swaps is zero. We still have to compare each item in the list to each other item in the list on each pass through the algorithm. The first time through, we compare the first item in the list to all other items in the list, so the number of comparisons is (N-1). The second time through, we compare the second item in the list to the remaining items in the list, so the number of comparisons is (N-2). It turns out that the total number of comparisons for selection sort in the best case is (N − 1) + (N − 2) + ... + 2 + 1. This equation simplifies to N(N + 1)/2 − 1, which is approximately N2. Thus, even in the best case, selection sort requires **O(n²)** comparisons.  

The worst case for selection sort occurs when the first item in the list is the largest, and the rest of the list is in order. In this case, we perform one swap on each pass through the algorithm, so the number of swaps is N. The number of comparisons is the same as in the best case, **O(n²)**.  

The average case requires the same number of comparisons, **O(n²)**, and roughly N/2 swaps. Thus, the number of swaps in the average case is **O(n)**.  

### Insertion sort  

*Insertion sort* is a simple sorting algorithm that is relatively efficient for small lists and mostly sorted lists, and often is used as part of more sophisticated algorithms. It works by taking elements from the list one by one and inserting them in their correct position into a new sorted list. In arrays, the new list and the remaining elements can share the array's space, but insertion is expensive, requiring shifting all following elements over by one.  

Best case: list is already sorted, number of comparisons is (n − 1) or **O(n)**.  

Worst case: reversed list; each iteration shifts the element all the way down **O(n²)**.
