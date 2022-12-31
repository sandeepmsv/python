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

def identicalTrees(root1,root2):
    result1=[]
    result2 = []
    result1= preorder(root1,result1)
    result2 = preorder(root2,result2)
    for value1,value2 in zip(result1,result2):
        if value1 != value2:
            return False
        return True
            
def preorder(root,result):
    if root is None:
        return 
    result.append(root.data)
    preorder(root.left)
    preorder(root.right)
    
    
       