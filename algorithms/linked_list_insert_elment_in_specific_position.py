"""
Insert a node at a specific position in a linked list

From <https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem> 

This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.
Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position and return the head node.
A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.
Example
 refers to the first node in the list 

Insert a node at position  with . The new list is 
Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.
insertNodeAtPosition has the following parameters:
• head: a SinglyLinkedListNode pointer to the head of the list
• data: an integer value to insert as data in your new node
• position: an integer position to insert the new node, zero based indexing
Returns
• SinglyLinkedListNode pointer: a reference to the head of the revised list
Input Format
The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer , the data of the node that is to be inserted.
The last line contains an integer .
Constraints
• , where  is the  element of the linked list.
• .
Sample Input
3
16
13
7
1
2
Sample Output
16 13 1 7
Explanation
The initial linked list is . Insert  at the position  which currently has  in it. The updated linked list is .

From <https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem> 

My code:
#!/bin/python3
import math
import os
import random
import re
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
#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(llist, data, position):
    listIter = llist
    i =0
    while i < position -1:
        listIter = listIter.next
        i+= 1
    newNode = SinglyLinkedListNode(data)
    newNode.next = listIter.next
    listIter.next = newNode
    return llist


"""