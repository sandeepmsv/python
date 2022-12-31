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
def solve(root):
    if root is None:
        return True
    return solveSymmetrical(root.left,root.right)
def solveSymmetrical(first,second):
    if not first or not second:
        return first == second
    if first.data != second.data:
        return False
    # recursively check the answer
    return solveSymmetrical(first.left,second.right) and solveSymmetrical(first.right,second.left)

    
        
    


    