class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
'''
1. Search for the value
2. connecting the left and right subtree
3. 
'''
def deleteInBinarySearchTree(root,k):
    # value given is k
    current = root
    while current:
        if current.data>k:
            if current.left is not None and current.left.data ==k:
                current.left = connectLeftAndRightSubTree(current.left)
                break
                
            else:
                current = current.left
        else:
            if current.right is not None and current.right.data == k:
                current.right = connectLeftAndRightSubTree(current.right)
                break
            else:
                current = current.right
    return root
def connectLeftAndRightSubTree(root):
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    # else, I know both left and right subtree exists, so I have to connect them
    rightSubTree = root.right
    leftSubTreeRightMostNode = getRightMostNode(root.left)
    leftSubTreeRightMostNode.right = rightSubTree
    return root.left
    
def getRightMostNode(root):
    while root:
        root = root.right
    return root  
