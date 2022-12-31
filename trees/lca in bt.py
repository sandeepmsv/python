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
    

def solve(root,node1,node2):
    ans = lca(root,node1,node2) # lca -----> lowest common Ancestor
    return ans
def lca(root,n1,n2):
    if not root:
        return None
    if root in [n1,n2]:
        return root
    leftCallValue = lca(root.left,n1,n2)
    rightCallValue = lca(root.right,n1,n2)
    if leftCallValue is None:
        return rightCallValue
    elif rightCallValue is None:
        return leftCallValue
    else: # when both left and right call return some value which is not None
        return root
    
     
     
     
    