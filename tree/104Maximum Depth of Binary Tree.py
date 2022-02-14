# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        res=0
        stk=[(root,0)]
        
        while stk:
            cur,dep=stk.pop()
            if not cur:
                if res<dep:
                    res=dep
                continue
            
            stk.append((cur.left,dep+1))
            stk.append((cur.right,dep+1))
            
        return res
        