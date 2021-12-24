# Merge Sort
## Merge Operation
The most fundamental operation of the Merge Sort, is the `merge` operations, which can take a number of sorted arrays and merge them into another sorted array.
The most common of which is a **Two Way Merge**, which takes two arrays as input and merges them. 
The most general form of which is an `m` Way Merge, but these can be modeled with a repetitive 2-way merge. 

???+ example "Two Way Merge"
  
    `[0, 2, 4, 6]` `[0, 3, 6, 9]` --> `[0, 0, 2, 3, 4, 6, 6, 9]`
    ```mermaid
    graph TD
    D[[0, 2, 4, 6]] --> C{Merge}
    E[[0, 3, 6, 9]] --> C
    C --> B[[0, 0, 2, 3, 4, 6, 6, 9]]
    ```

## Two Way Merge Sort
Break down an array to be sorted, till there are only two elements. An array with only one element is sorted, by virtue of having only one element.

## Merge Sort
A recursive algorithm. $\theta(n * log n)$

### Time Complexity
Time complexity of Two Way Merge sort is $O(n * log n)$

### Applications
* Large Sized List
* Linked List
  * It is really easy to perform merge operation on Linked List, we do not need to create temporary 3rd array.
* External Sorting of huge data
  * When the data that needs to be sorted exceed the available RAM, merge sort can be used to piece-wise sorting and while storing the intermediate result on disk.
* Stable
  * Order of duplicates is maintained.

#### Cons
* Extra Place
  * Not an inplace sort
  * This is however not need in the case of LinkedList
* No small problem, for a small size it is slower.
  * Insertion Sort $O(n^2)$ -> Also Stable
  * Merge Sort $O(n log n))$
  * Bubble Sort $O(n^2)$ -> Also Stable
* Recursive, all recursive algorithms use the stack, need more memory due the requirements of many stacks.
