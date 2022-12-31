# print all the nodes at a distance of k
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
    
    
    
def nodesAtDistancedK(root,target,k):
    parent ={} #empty dictionary
    initializeParent(parent,root)
    queue = [target]
    distance = k
    visited = set()
    visited.add(target)
    while queue:
        n = len(queue)
        for _  in range(n):
            currentNode = queue[0]
            queue.pop()
            if currentNode.left and currentNode.left not in visited:
                visited.add(currentNode.left)
                queue.append(currentNode.left)
            if currentNode.right and currentNode.right not in visited:
                visited.add(currentNode.right)
                queue.append(currentNode.right)
            if currentNode in parent and parent[currentNode] not in visited:
                visited.add(parent[currentNode])
                queue.append(parent[currentNode])
        distance +=1
        if distance>k:
            break
        return queue
    
        
        
            
def initializeParent(parent,root):
    queue = [root]
    while queue: #while queue is not empty
        currentNode = queue[0]
        queue.pop()
        if currentNode.left:
            parent[currentNode.left] = currentNode
            queue.append(currentNode.left)
        if currentNode.right:
            parent[currentNode.right] = currentNode
            queue.append(currentNode.right)  