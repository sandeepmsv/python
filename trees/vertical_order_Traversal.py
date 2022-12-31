# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#         """
#              10 
#         7         6
#     5      60
        
#         """
# def createtree():
#     root = TreeNode(10)
#     root.left = TreeNode(7)
#     root.right = TreeNode(6)
#     root.left.left = TreeNode(5)
#     root.left.right = TreeNode(60)
    
from collections import deque
 
 
# A class to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
def printVertical(root):
 
    # base case
    if root is None:
        return
 
    # create a dictionary to store the vertical order of binary tree nodes
    d = {}
 
    # create an empty queue for level order traversal.
    # `It` stores binary tree nodes and their horizontal distance from the root.
    q = deque()
 
    # enqueue root node with horizontal distance as 0
    q.append((root, 0))
 
    # loop till queue is empty
    while q:
 
        # dequeue front node
        node, dist = q.popleft()
 
        # insert front node value into the dictionary using its horizontal distance
        # as the key
        d.setdefault(dist, []).append(node.key)
 
        # enqueue non-empty left and right child of the front node
        # with their corresponding horizontal distance
        if node.left:
            q.append((node.left, dist - 1))
 
        if node.right:
            q.append((node.right, dist + 1))
 
    # print the dictionary
    for key in sorted(d.keys()):
        print(d.get(key))

            
                    
        