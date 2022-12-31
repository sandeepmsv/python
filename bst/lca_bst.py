# LCA in bst
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def lcaInBinarySearchTree(root,value1,value2):
    current = root
    ans = None
    while current:
        if current.data>value1 and current.data>value2:
            current = current.left
        elif current.data<value1 and current.data<value2:
            current = current.right
        else:
            ans = current.data
            break
    return ans
            