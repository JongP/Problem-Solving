# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        
        
        def trav(node,path):
        
            path = (path<<1) + node.val

            
            
            if node.left:
                trav(node.left,path)
            if node.right:
                trav(node.right,path)
        
            if not node.left and not node.right:
                self.ans+=path

        trav(root,0)
        
        
        return self.ans

#exampel solution
#preorder==DFS
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def helper(root,nums):
            
            nums += str(root.val)
            if root.left:
                helper(root.left,nums)
            if root.right:
                helper(root.right,nums)
            if not root.left and not root.right:
                self.total += int(nums,2)
                return    
        

        helper(root, "")
        return self.total
        