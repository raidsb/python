"""
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

    Enqueue: add a new element to the end of the queue.
    Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process
queries, where each query is one of the following

types:

    1 x: Enqueue element 

    into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.

Input Format

The first line contains a single integer,
, denoting the number of queries.
Each line of the subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query is followed by an additional space-separated value, , denoting the value to be enqueued.

https://www.hackerrank.com/challenges/one-month-preparation-kit-queue-using-two-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three

"""

# My code
class Q:
    def __init__(self):
        pass
    
    stack1 = []
    stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    # just for reference. not tested
    def dequeue_long_method_using_stack2(self):
        # move all elements from stack1, those need to move to the other stack
        moved_elements = self.stack1[1:len(self.stack1) - 1].reverse()
        self.stack2.append(moved_elements)
        del self.stack1[1:]
        
        # pop the last item in the stack1 which equals to dequeue
        self.stack1.pop()
        
        # bring back the moved elements to stack1
        de_moved_elements = moved_elements.reverse()
        self.stack1.append(de_moved_elements)
        self.stack2.clear()
    
    def dequeue(self):
        self.stack1.pop(0)
        
    def get_front(self):
        return self.stack1[0]
    

number_q = int(input())
q = Q()

for i in range(number_q):
    query = input().split()
    if int(query[0]) == 1:
        q.enqueue(query[1])
    elif int(query[0]) == 2:
        q.dequeue()
    else:
        print(q.get_front())