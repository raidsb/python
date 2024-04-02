"""
This challenge is part of a tutorial track by MyCodeSchool

Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

Example
refers to
refers to The new list is

Function Description

Complete the mergeLists function in the editor below.

mergeLists has the following parameters:

    SinglyLinkedListNode pointer headA: a reference to the head of a list
    SinglyLinkedListNode pointer headB: a reference to the head of a list

Returns

    SinglyLinkedListNode pointer: a reference to the head of the merged list

Input Format

The first line contains an integer

, the number of test cases.

The format for each test case is as follows:

The first line contains an integer
, the length of the first linked list.
The next lines contain an integer each, the elements of the linked list.
The next line contains an integer , the length of the second linked list.
The next lines contain an integer each, the elements of the second linked list. 

https://www.hackerrank.com/challenges/one-month-preparation-kit-merge-two-sorted-linked-lists/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three

"""

def search_for_position_in_sorted_list(head, data):
    while True:
        if data >= head.data:
            if head.next is not None:
                if data >= head.next.data:
                    head = head.next
                else:
                    return head, 'after'
            else:
                return head, 'after'
        elif data < head.data:
            return head, 'before'        
        
def mergeLists(head1, head2):
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
            
    while head2 is not None:
        head_to_insert, position = search_for_position_in_sorted_list(head1, head2.data)
        if position == 'after':
            head1_temp = head_to_insert.next
            head2_temp = head2.next
            head_to_insert.next = head2
            head2.next = head1_temp
            head2 = head2_temp
        else:
            head2_temp = head2.next
            head2.next = head_to_insert
            head1 = head2
            head2 = head2_temp
    
    return head1