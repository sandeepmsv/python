# Floor in bst
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def floorInBinarySearchTree(root,k):
    # value given is k,O(logn)
    floorValue = -1
    while root:
        if root.data ==k:
            floorValue = root.data
            break
        if k>root.data:
            floorValue = root.data
            root = root.right
        else:
            root = root.left
    return floorValue
       