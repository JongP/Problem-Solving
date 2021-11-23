# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global answer
        answer=0
        self.dfs(root,0)
        return answer
    
    def dfs(self,node,number):
        global answer
        number=number*10+node.val
        
        
        if not node.left and not node.right:
            answer+=number
            return
        
        if node.left:
            self.dfs(node.left,number)
        if node.right:
            self.dfs(node.right,number)
        