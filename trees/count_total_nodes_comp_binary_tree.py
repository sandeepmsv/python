# count total nodes in a complete binary tree
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
def countTotalNodesInCompleteBinaryTree(root):
    result = nodesCount(root)
    return result
def nodesCount(root):
    if not root:
        return root
    leftSubtree = countHeight1(root.left)
    rightSubtree = countHeight2(root.right)
    if leftSubtree == rightSubtree:
        return (2**rightSubtree)-1
    #else
    return 1+nodesCount(root.left)+nodesCount(root.right)
def countHeight1(node):
    heigth = 0
    while node:
        height +=1
        node = node.left
    return height
def countHeight2(node):
    height = 0
    while node:
        height+=1
        node = node.right
    return height
    
    
    
    