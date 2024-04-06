"""
Compare two linked lists

From <https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen> 
 
This challenge is part of a tutorial track by MyCodeSchool
You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return . Otherwise, return .
Example

The two lists have equal data attributes for the first  nodes.  is longer, though, so the lists are not equal. Return .
Function Description
Complete the compare_lists function in the editor below.
compare_lists has the following parameters:
• SinglyLinkedListNode llist1: a reference to the head of a list
• SinglyLinkedListNode llist2: a reference to the head of a list
Returns
• int: return 1 if the lists are equal, or 0 otherwise
Input Format
The first line contains an integer , the number of test cases.
Each of the test cases has the following format:
The first line contains an integer , the number of nodes in the first linked list.
Each of the next  lines contains an integer, each a value for a data attribute.
The next line contains an integer , the number of nodes in the second linked list.
Each of the next  lines contains an integer, each a value for a data attribute.
Constraints
Output Format
Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.
The output is handled by the code in the editor and it is as follows:
For each test case, in a new line, print  if the two lists are equal, else print .
Sample Input
2
2
1
2
1
1
2
1
2
2
1
2
Sample Output
0
1
Explanation
There are  test cases, each with a pair of linked lists.
• In the first case, linked lists are: 1 -> 2 -> NULL and 1 -> NULL
• In the second case, linked lists are: 1 -> 2 -> NULL and 1 -> 2 -> NULL

From <https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen> 


My code: 
"""

#!/bin/python3
import os
import sys
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)
# Complete the compare_lists function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    llist1Temp = llist1
    llist2Temp = llist2
    ok = 1
    
    while ok == 1 and llist1Temp is not None:
        # if either of them is None but the other is not
        if llist1Temp.next != llist2Temp.next and (llist1Temp.next is None or llist2Temp.next is None):
            return 0            
        
        if llist1Temp.data != llist2Temp.data:
            return 0
        
        llist1Temp = llist1Temp.next
        llist2Temp = llist2Temp.next
        
    return ok            
