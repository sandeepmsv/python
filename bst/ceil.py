class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def ceilInBinarySearchTree(root,k):
    # value is k 
    ceilValue = -1
    while root: # while my root is not None, I will Continue
        if root.data ==k:
            ceilValue = root.data
            break
        if k>root.data:
            root = root.right
        else:
            ceilValue = root.data
            root = root.left
    return ceilValue
    