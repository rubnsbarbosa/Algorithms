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


### Quick sort  

*Quicksort* is in fact a very fast sorting algorithm. The basic idea behind quicksort is this: Specify one element in the list as a “pivot” point. Then, go through all of the elements in the list, swapping items that are on the “wrong” side of the pivot. In other words, swap items that are smaller than the pivot but on the right side of the pivot with items that are larger than the pivot but on the left side of the pivot. Once you’ve done all possible swaps, move the pivot to wherever it belongs in the list. Now we can ignore the pivot, since it’s in position, and repeat the process for the two halves of the list (on each side of the pivot). We repeat this until all of the items in the list have been sorted.  

Quicksort is an example of a divide and conquer algorithm. Quicksort sorts a list effectively by dividing the list into smaller and smaller lists, and sorting the smaller lists in turn.  

The best case of quicksort occurs, obviously, when the list is already sorted. For this algorithm, the best case resembles the average case in terms of performance. The average case occurs when the pivot splits the list in half or nearly in half on each pass. Each pass through the algorithm requires N comparisons. But how many passes does quicksort take? Recall that every time we divide something in half repeatedly, as in binary search, the number of operations is approximately **log2 N**. So, the number of passes through the algorithm is approximately **log2N**, and thus the number of comparisons in the average and best cases is
**O(n log n)**. The number of swaps differs in the best and average cases: for the best case, we have no swaps, but for the
average case, by the same reasoning, we have **O(n log n)** swaps.  

The worst case for quicksort occurs when the pivot is always the largest or smallest item on each pass through the list. In this instance, we do not split the list in half or nearly in half, so we do N comparisons over roughly N passes, which means that in the worst case quicksort is closer to **O(n²)** in performance. For the same reason, the number of swaps in the worst case can be as high as **O(n²)**.
