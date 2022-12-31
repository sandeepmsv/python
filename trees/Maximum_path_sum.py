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
def maxPathSum(root):
    maxSum = [0]
    solve(root,maxSum)
    return maxSum[0]
def solve(root,maxSum):
    if not root:
        return 0
    leftSum = solve(root.left,maxSum)
    rightSum = solve(root.right,maxSum)
    #VVIMP
    if leftSum<0: leftSum = 0
    if rightSum<0: rightSum = 0
    maxSum[0] = max(maxSum[0],root.data+leftSum+rightSum)
    return root.data+max(leftSum,rightSum)
    


    