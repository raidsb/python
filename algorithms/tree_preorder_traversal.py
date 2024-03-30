"""
Tree: Preorder Traversal

From <https://www.hackerrank.com/challenges/tree-preorder-traversal/problem> 

Complete the  function in the editor below, which has  parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.
Input Format
Our test code passes the root node of a binary tree to the preOrder function.
Constraints
 Nodes in the tree 
Output Format
Print the tree's preorder traversal as a single line of space-separated values.
Sample Input
     1
      \
       2
        \
         5
        /  \
       3    6
        \
         4  
Sample Output
1 2 5 3 4 6 
Explanation
The preorder traversal of the binary tree is printed.

From <https://www.hackerrank.com/challenges/tree-preorder-traversal/problem> 
"""

My code:
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    leftSide = root.left
    rightSide = root.right 
    print(root.info,end=' ') 
    if leftSide is not None:
        preOrder(leftSide)
    if rightSide is not None: 
        preOrder(rightSide)   