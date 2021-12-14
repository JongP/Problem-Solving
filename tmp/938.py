# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[0]
        
        def inorderTraverse(node):
            if not node:
                return
            
            
            if node.val>=low:
                inorderTraverse(node.left)
            
            if node.val >= low and node.val<=high:
                ans[0]+=node.val
            
            if node.val<=high:
                inorderTraverse(node.right)
            
            
        
        
        inorderTraverse(root)
        
        
        return ans[0]