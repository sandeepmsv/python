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
def diameterOfBinaryTree(root):
    diameter = [0]
    solve(root,diameter)
    return diameter[0]
def solve(root,diameter):
    if not root: # if root is None
        return 0
    leftHeight = solve(root.left,diameter)
    rightHeight = solve(root.right,diameter)
    diameter[0] = max(diameter,leftHeight+rightHeight)
    return 1+max(leftHeight,rightHeight)

        
    