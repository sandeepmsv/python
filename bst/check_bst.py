# check if a tree is binary tree or binary search tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def checkBinarySearchTree(root):
    return solve(root,-float("inf"),float("inf"))


def solve(root,leftValue,rightValue):
    if not root:
        return True
    if root.data>=rightValue or root.data<= leftValue:
        return False
    # else, Valid Node, I will check for further nodes
    return solve(root.left,leftValue,root.data) and solve(root.right,root.data,rightValue)


        
    
