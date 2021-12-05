# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def goDFS(node) -> tuple:
            if not node:
                return (0,0)

            if not node.right and not node.left:
                return (node.val,0)
            
            le1,le2=goDFS(node.left)
            ri1,ri2=goDFS(node.right)
            
            return (max(node.val+le2+ri2,le1+ri1),le1+ri1)
            
            
        dp1,dp2=goDFS(root)
        
        
        
        return max(dp1,dp2)