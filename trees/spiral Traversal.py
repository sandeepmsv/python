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
def spiralOrder(root): # zig zag traversal
    queue = [root]
    ans = []
    while queue:
        levelNodes = []
        n = len(queue)
        for i in range(n):
            currentNode = queue[0]
            queue.pop(0)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.apped(currentNode.right)
            levelNodes.apend(currentNode)
        ans.append(levelNodes)
    for i in range(1,len(ans),2):
        ans[i] = ans[i][::-1]
    return ans


        
        

    