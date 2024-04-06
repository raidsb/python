Algorithms:
/##################################################################################
#Heap queue also known as heapq: Yes, the heapq module in Python implements a priority queue using a binary heap.# 
##############################################################################
A binary heap is a complete binary tree where each node has a value that is less than or equal to the values of its 
children (in a min heap) or greater than or equal to the values of its children (in a max heap). This property ensures 
that the smallest (or largest, in the case of a max heap) element is always at the root of the tree.

However, Python's heapq module does not directly expose a tree-like structure. Instead, it uses a regular list to represent 
the binary heap. The elements of the list are ordered in such a way that the root of the binary heap is at index 0, and for 
any element at index i, its left child is at index 2*i + 1 and its right child is at index 2*i + 2.

The heapq module provides functions to perform heap operations on this list, such as:

    heapify: Converts a regular list into a heap in linear time.
    heappush: Adds a new element to the heap while maintaining the heap property.
    heappop: Removes and returns the smallest (or largest) element from the heap.
    heappushpop: Adds a new element to the heap and returns the smallest (or largest) element.
    heapreplace: Removes and returns the smallest (or largest) element from the heap, then adds a new element.

These functions ensure that the heap property is maintained after each operation, allowing efficient access to the smallest (or largest) 
element in the heap. 

The heapq module in Python provides an efficient implementation of a priority queue (min-heap) using a list. It is a good choice 
for this problem because:

    - Efficiency: The heapq module provides efficient operations for maintaining the heap property while adding and removing 
	elements from the heap. This makes it suitable for scenarios where you need to repeatedly find and process elements with the 
	smallest value efficiently.

    - Ease of Use: heapq is part of Python's standard library, so you don't need to install any additional packages to use it. 
	It provides simple and intuitive functions like heapify, heappush, and heappop for working with heaps.

    - Space Complexity: The heapq implementation typically uses less memory compared to other data structures like binary search 
	trees while still providing logarithmic time complexity for basic heap operations.

    - Flexibility: heapq allows you to create a min-heap from an existing list and perform operations like push and pop efficiently. 
	It's flexible enough to handle a wide range of scenarios where a priority queue is needed.

Overall, heapq provides a good balance of efficiency, ease of use, and flexibility, making it a suitable choice for solving problems 
involving priority queues, such as the "Jessie and Cookies" problem on HackerRank.

########################
How to determine when to use heapq? #
########################
You can consider using the heapq module in Python when you need to efficiently manage a collection of elements where you 
frequently need to access the smallest (or largest) element. Some common scenarios where you might use heapq include:

