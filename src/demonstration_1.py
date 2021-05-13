"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    /
   5

Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val <= self.val:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = TreeNode(val)
            else:
                self.left.insert(val)

        else:
            # the value must go right
            if self.right is None:
                self.right = TreeNode(val)
            else:
                # let the right hand Node figure it out
                self.right.insert(val)

array = []

def inorder_traversal(root):
    # Your code here
    if root.left:
        inorder_traversal(root.left)

    array.append(root.val)

    if root.right:
        inorder_traversal(root.right)

    return array

root = TreeNode(1)
root.insert(3)
root.insert(5)

inorder_traversal(root)
print(array)