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
    
def rootNodePath(root,targetNode):
    path = []
    getPath(root,targetNode,path)
    return path
def getPath(root,targetNode,path):
    if not root: return False
    path.append(root.data)
    if root.data==targetNode: return True
    if getPath(root.left,targetNode,path) is True or getPath(root.right,targetNode,path) is True:
        return True
    # since both of them fare False
    path.pop()
    return False

    
    
    
    
      