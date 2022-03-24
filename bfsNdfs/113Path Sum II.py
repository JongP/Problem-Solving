# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        
        def dfs(node,total,path):
            if not node: return
            
            total+=node.val
            path.append(node.val)
            if not node.left and not node.right and total==targetSum:
                res.append(path.copy())
            
            dfs(node.left,total,path)
            dfs(node.right,total,path)
            path.pop()
            
            
            
        
        dfs(root,0,[])
            
        
        return res