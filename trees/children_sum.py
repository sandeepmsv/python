#children Sum
'''
ForEvery Node in the Binary tree is the sum of its children node
is equal to parent node data

'''
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        """
             10 
        7         6
    5      60
        
        """
def createtree():
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(60)
def childrenSumProperty(root):
    if not root:
        return
    childSum = 0
    if root.left: childSum += root.left.data
    if root.right: childSum==root.right.data
    if childSum<root.data:
        if root.left:root.left.data = root.data
        elif root.right:root.right.data = root.data
    else: #childSum >=root.data 
        root.data = childSum
    childrenSumProperty(root.left)
    childrenSumProperty(root.right)
    newRootData = 0
    if root.left:
        newRootData += root.left.data
    if root.right:
        newRootData += root.right.data
    if root.left or root.right:
        root.data = newRootData
    
        
