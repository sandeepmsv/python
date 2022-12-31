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
def maximum_depth(root):
    result = solve(root)-1 # depth is basically the number of jumps
    # if the depth/height is considered in terms of level,
    # answer is sove(root)
    return result
def solve(root):
    if root is None:
        return 0
    leftHeight = solve(root.left)
    rightHeight = solve(root.right)
    return 1+max(leftHeight,rightHeight)

    
   

    