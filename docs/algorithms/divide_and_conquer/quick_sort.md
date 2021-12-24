# Quick Sort
* Quick Sort another sorting algorithms that uses divide and conquer strategy.

## Pivot Element
* A fundamental part of quick sort is a something called a **Pivot Element**, it is the element in the array that is in the right place.
* By that we mean, all the elements to the Pivot Element's left are lower than it and all elements to its right are greater than it.

???+ example "Pivot element"
    For example, in this array `[8, 4, 3, 10, 12, 11, 32, 47]`, `10` would be a pivot element.

## Algorithm
* Pivot elements allow use to apply to divide and conquer technique to the sorting of the array. 
* The two new and separate sub-problems here then would be, the sorting of two slices of the arrays to the left and right of the pivot element.
* This process can be applied recursively until all elements are in their right place.

### Finding a Pivot element
* Portioning is the process of finding the pivot element and create one if non-exists.

## Analysis
### Time Complexity
* The time complexity of this recursive algorithm, where we partition each array into two arrays at each level of recursion.
* Best Case
  * If the Pivot element at every recursion is a the median of that array, that it is apears at the middle of the array.
  * Then, the array is divided in half at each recursion.
  * The Time Complexity would be $O(n * logn)$.
  * But, we do not know the median upfront, and cannot ensure that the median and pivot element are the same.

???+ example "Pivot element"
    For example, here `[1, 2, 3, 4, 5, 6, 7]`, if `4` is chosen as a pivot element, it is also the median of the array.
    The array would be partitioned in two equal half for the next recursion.

* Worst Case
  * Worst case occurs, when the partition occurs at the beginning of the list.
  * The Time Complexity would be $O(n^2)$.
???+ example "Pivot element"
  For example, here `[2, 4, 8, 10, 16, 18, 17]`, if `2` is chosen as a pivot element.
  Then the array would be partitioned, with only on element on the one of the partitions.

#### Improving Worst Case
* Always select the middle element as pivot.
* Select a random element as pivot.

### Memory Complexity
* Best case is $log n$, as there $log n$ recursions and stacks. 
* Worst case is $n$, as there $n$ recursions and stacks. 
