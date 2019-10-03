## Searching algorithms  

There are two types of search algorithms: algorithms that don’t make any assumptions about the order of the list, and algorithms that assume the list is already in order.  
We use the term search to indicate the item for which we are searching. We assume the list to search is an array of integers, although these algorithms will work just as well on any other primitive data type (doubles, characters, etc.). We refer to the array elements as items and the array as a list.  

### Linear Search  

The simplest search algorithm is linear search algorithm (also known as sequential search). In linear search, we look at each item in the list in turn, quitting once we find an item that matches the search term. As the name suggests, the complexity of linear search is linear.  

Analysis:  

* Best case: The best case occurs when the search term is in the first slot in the array, we immediately find the element. The number of comparisons in this case is 1 or **O(1)**.  

* Worst case: The worst case occurs when the search term is in the last slot in the array, or is not in the array. The number of comparisons in this case is equal to the size of the array. If our array has N items, then it takes N comparisons in the worst case or **O(n)**.  

* Average case: On average, the search term will be somewhere in the middle of the array. The number of comparisons in this case is approximately N/2 ∈ **O(n)**.  

In both the worst case and the average case, the number of comparisons is proportional to the number of items in the array, N. Thus, we say in these two cases that the number of comparisons is order N, or O(N) for short. For the best case, we say the number of comparisons is order 1, or O(1) for short.

### Binary Search  

Binary search exploits the ordering of a list.  
The idea behind binary search is that each time we make a comparison, we eliminate half of the list, until we either find the search term or determine that the term is not in the list.  
We do this by looking at the middle item in the list, and determining if our search term is higher or lower than the middle item.  
If it’s lower, we eliminate the upper half of the list and repeat our search starting at the point halfway between the first item and the middle item.  
If it’s higher, we eliminate the lower half of the list and repeat our search starting at the point halfway between the middle item and the last item.  

Analysis:  

* Best case: The best case for binary search still occurs when we find the search term on the first try. In this case, the search term would be in the middle of the list. As with linear search, the best case for binary search is **O(1)**, since it takes exactly one comparison to find the search term in the list.  

* Worst case: The worst case for binary search occurs when the search term is not in the list, or when the search term is one item away from the middle of the list, or when the search term is the first or last item in the list. How many comparisons does the worst case take? To determine this, let’s look at a few examples.  

Suppose we have a list of four integers: {1, 4, 5, 6}. We want to find 2 in the list. According to the algorithm, we start at the second item in the list, which is 4. Our search term, 2, is less than 4, so we throw out the last three items in the list and concentrate our search on the first item on the list, 1. We compare 2 to 1, and find that 2 is greater than 1. At this point, there are no more items left to search, so we determine that 2 is not in the list. It took two comparisons to determine that 2 is not in the list.

Now suppose we have a list of 8 integers: {1, 4, 5, 6, 9, 12, 14, 16}. We want to find 9 in the list. Again, we find the item at the midpoint of the list, which is 6. We compare 6 to 9, find that 9 is greater than 6, and thus concentrate our search on the upper half of the list: {9, 12, 14, 16}. We find the new midpoint item, 12, and compare 12 to 9. 9 is less than 12, so we concentrate our search on the lower half of this list (9). Finally, we compare 9 to 9, find that they are equal, and thus have found our search term at index 4 in
the list. It took three comparisons to find the search term.

If we look at a list that has 16 items, or 32 items, we find that in the worst case it takes 4 and 5 comparisons, respectively, to either find the search term or determine that the search term is not in the list. In all of these examples, the number of comparisons is log2 N. This is much less than the number of comparisons required in the worst case for linear search! In general, the worst case for binary search is order **log N**, or **O(log N)**.

* Average case: The average case occurs when the search term is anywhere else in the list. The number of comparisons is roughly the same as for the worst case, so it also is **O(log N)**.

In general, anytime an algorithm involves dividing a list in half, the number of operations is **O(log N)**.
