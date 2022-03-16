class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(node):
            if not node:
                return 0
            
            lH,rH=helper(node.left),helper(node.right)
            
            return max(lH,rH)+1 if lH!=-1 and rH!=-1 and abs(lH-rH)<=1 else -1
        
        
        return helper(root)!=-1