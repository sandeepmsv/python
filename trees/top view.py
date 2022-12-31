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
def topViewOfBinaryTree(root):
    queue = [(root,0)]
    verticalPathDictionary = {}
    while queue:
        currentNode,verticalPosition = queue[0]
        queue.pop()
        if verticalPosition not in verticalPathDictionary:
            verticalPathDictionary[verticalPosition] = [currentNode.data]
        if currentNode.left:
            queue.append((currentNode.left,verticalPosition-1))
        if currentNode.right:
            queue.append((currentNode.right,verticalPosition+1))   
    for key in sorted(verticalPathDictionary.keys()):
        print(verticalPathDictionary[key])