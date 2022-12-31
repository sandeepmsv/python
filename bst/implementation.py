class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def searchInBinarySearchTree(root,k):
    #value is k
    while(root is not None) and (root.data !=k):
        # I know left part is having value smaller than root value
        if k<root.data:
            root = root.left
        else:
            root = root.right
    return root

        