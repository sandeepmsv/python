class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insertInBinarySearchTree(root,k):
    # value given is k
    if root is None:
        return Node(k)
    current = root
    while True: # while 1
        if current.data <=k:
            if current.right is None:
                current.right = Node(k)
                break
            else:
                current = current.right
        else:
            if current.left is None:
                current.left = Node(k)
                break
            else:
                current = current.left
    return root

        
        