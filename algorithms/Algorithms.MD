Algorithms:
####################################################################################
#                              Array Problem  solving tips                         #
####################################################################################

Here are some tips to help you solve array data structure problems more effectively:
1 - Understand the Problem: Read the problem statement carefully and make sure you understand what is required. 
    Identify the input constraints, the expected output, and any special conditions.

2-  Choose the Right Data Structure: While the problem may involve arrays, consider if other data structures like 
    sets, maps, or heaps could be useful in solving the problem more efficiently.

3-  Start with Brute Force: If you're unsure how to approach the problem, start with a brute force solution. 
    This involves trying every possible solution and checking if it meets the problem requirements. 
	Although brute force solutions are often not optimal, they can provide insights into more efficient approaches.

4-  Optimize: Once you have a working solution, analyze its time and space complexity. Look for opportunities to 
    optimize your solution by reducing time complexity (e.g., by eliminating unnecessary iterations) or 
	space complexity (e.g., by reusing variables instead of creating new ones).

5-  Use Two Pointers Technique: In problems involving arrays, the two pointers technique can be useful for 
    solving problems efficiently. This technique involves using two pointers to traverse the array simultaneously, 
	often allowing you to solve the problem in linear time.

6-  Consider Sorting: Sorting the array can simplify many array-related problems. It can help you identify patterns, 
    eliminate duplicates, or find specific elements more efficiently.

7-  Handle Edge Cases: Don't forget to handle edge cases such as empty arrays, arrays with only one element, or arrays 
    with negative numbers. These cases may require special treatment in your solution.

8-  Practice: Practice solving a variety of array-related problems on platforms like LeetCode, HackerRank, or Codeforces. 
    The more problems you solve, the better you'll become at identifying patterns and applying different techniques 
	to solve them.

9-  Review Solutions: After solving a problem, take the time to review and understand other solutions posted by the 
    community. You may learn new techniques or optimizations that can be applied to similar problems in the future.

Stay Persistent: Some problems may seem difficult at first, but don't get discouraged. Keep practicing, learning, 
and refining your problem-solving skills. With time and practice, you'll become more proficient at solving array 
data structure problems.

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

