# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def traverse(node)-> tuple:
            
            resMin,resMax=node.val, node.val
            
            if node.left:
                lMin,lMax=traverse(node.left)
                if lMax>=node.val:
                    return -1*math.inf, math.inf
                resMin=lMin
                
                
                
            if node.right:
                rMin,rMax=traverse(node.right)
                if rMin<=node.val:
                    return -1*math.inf, math.inf
                resMax=rMax
            
            return resMin,resMax
        
        return traverse(root)!=(-1*math.inf, math.inf)


#https://leetcode.com/problems/validate-binary-search-tree/discuss/32153/Python-version-based-on-inorder-traversal
class Solution:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)