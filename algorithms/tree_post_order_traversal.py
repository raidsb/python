"""
Tree: Postorder Traversal

From <https://www.hackerrank.com/challenges/tree-postorder-traversal/problem> 

Complete the  function in the editor below. It received  parameter: a pointer to the root of a binary tree. It must print the values in the tree's postorder traversal as a single line of space-separated values.
Input Format
Our test code passes the root node of a binary tree to the  function.
Constraints
 Nodes in the tree  
Output Format
Print the tree's postorder traversal as a single line of space-separated values.
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
4 3 6 5 2 1 
Explanation
The postorder traversal is shown.

From <https://www.hackerrank.com/challenges/tree-postorder-traversal/problem> 

The Algorithm
Post-order, LRN[edit]
	1. Traverse the left subtree by recursively calling the post-order function.
	2. Traverse the right subtree by recursively calling the post-order function.
	3. Access the data part of the current node (in the figure: position blue).
	The trace of a traversal is called a sequentialisation of the tree. The traversal trace is a list of each visited node. No one sequentialisation according to pre-, in- or post-order describes the underlying tree uniquely. Given a tree with distinct elements, either pre-order or post-order paired with in-order is sufficient to describe the tree uniquely. However, pre-order with post-order leaves some ambiguity in the tree structure.[7]
From <https://en.wikipedia.org/wiki/Tree_traversal#Post-order> 

"""

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=' ')