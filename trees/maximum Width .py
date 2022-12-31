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
def maximumWidthofBinaryTree(root):
    queue = [root]
    maxwidth = 0
    while 1:
        start = False
        end = False
        n = len(queue)
        pos =1
        for _ in range(n):
            currentNode = queue[0]
            queue.pop()
            if currentNode is not None:
                if not start:
                    start = pos
                else:
                    end = pos
                queue.append(currentNode.left)
                queue.append(currentNode.right)
            else:
                queue.append(None)
                queue.append(None)
            pos += 1
        if start is False and end is False:
            break
        else:
            if start and end:
                maxWidth = max(maxWidth,(end-start)+1)
    return maxWidth
            

    