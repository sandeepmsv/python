


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
def boundaryTraversal(root):
    if root is None:
        return []
    path = []
    if root:
        path.append(root.data)
    leftBoundary(root.left,path)
    leafNodes(root,path)
    rightBoundary(root.right,path)
def leftBoundary(node,path):
    while node:
        # if the node is not a leaf node add it to the path
        if node.left or node.right:
            path.append(node.data)
        if node.left:
            node = node.left
        else:
            node = node.right
def leafNodes(root,path):
    if root.left is None and root.right is None:
        path.append(root.data)
        return
    if root.left:
        leafNodes(root.left,path)
    if root.right:
        leafNodes(root.right,path)
def rightBoundary(node,path):
    stack = []
    while node:
        if node.left or node.right:
            stack.append(node.data)
        if node.right:
            node = node.right
        else:
            node = node.left
    while stack:
        path.append(stack.pop())
        
            
            
        
        
