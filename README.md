# Data Structure & Algorithms

- IDE : PyCharm
- Python Version: 3.7

## Data Structures
* Organizing data in memory
* Processing the data
  
### Common Data Structures
* Array
* Linked List
* Stack
* Queue

### Advanced Data Structures
* Tree
* Heap
* Graph

## Searching Algorithms

### Linear Search

A simple approach is to do linear search, i.e
* Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
* If x matches with an element, return the index
* If x doesn’t match with any of elements, return -1

**Time Complexity** : O(n)

Linear search is rarely used practically because other search algorithms such as the binary search algorithm and hash tables allow 
significantly faster searching comparison to Linear search.


### Binary Search

Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the 
value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise 
narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

**Time Complexity** : O(Log n)

**Auxiliary Space**: O(1) in case of iterative implementation. In case of recursive implementation, O(Logn) recursion call stack space.

We basically ignore half of the elements just after one comparison.

1. Compare x with the middle element.
2. If x matches with middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
4. Else (x is smaller) recur for the left half.


### Fibonacci Search

Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.

**Similarities with Binary Search**
1. Works for sorted arrays
2. A Divide and Conquer Algorithm
3. Has Log n time complexity

**Differences with Binary Search**
1. Fibonacci Search divides given array in unequal parts
2. Binary Search uses division operator to divide range. Fibonacci Search doesn’t use /, but uses + and -. The division operator may be costly on some CPUs.
3. Fibonacci Search examines relatively closer elements in subsequent steps. So when input array is big that cannot fit in CPU cache or even in RAM, Fibonacci Search can be useful.
