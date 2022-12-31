class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def serializeBinaryTree(root):
    if not root:
        return ""
    value = ""
    queue = [root]
    # "12345NNNNNNN"
    
    while queue:
        current = queue[0]
        queue.pop(0)
        if current is None:
            value +="N"
        else:
            # current is a particular node
            value += str(current.data)+" "
            queue.append(current.left)
            queue.append(current.right)
    return value # string and my serialization process is over
        
def deserializeBinaryTree(value):
    if value =="":
        return None
    value =value.split(" ")
    root = Node(int(value[0]))
    queue = [root]
    idx = 1
    while queue:
        current = queue[0]
        queue.pop(0)
        # current can be one of these -> "N","int value"
        if current !="N": # its some integer string 
            leftChild = Node(value[idx])
            current.left = leftChild
            queue.append(leftChild)
            idx+=1
        if current!="N":
            rightChild = Node(value[idx])
            current.right = rightChild
            queue.append(rightChild)
            idx+=1
            
            
                        