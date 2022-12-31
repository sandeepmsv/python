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
def balanced_binarytree(root):
    result = solve(root)
    if result == -1:
        return False # not a balances binary tree
    return True
def solve(root):
    if not root:
        return 0
    leftHeight = solve(root.left)
    if leftHeight == -1: return -1
    rightHeight = solve(root.right)
    if rightHeight == -1: return -1
    if abs(leftHeight - rightHeight)>1: return -1
    # Other Case
    return 1+max(leftHeight,rightHeight)


    
    
    
    