# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def setPrefixSum(self,root,total):
        if not root: return
        
        root.prefixSum=total+root.val
        
        self.setPrefixSum(root.left,root.prefixSum)
        self.setPrefixSum(root.right,root.prefixSum)
        
        
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic={0:1}
        
        self.setPrefixSum(root,0)
        
        
        def trav(node,targetSum,dic):
            if not node: return 0
            
            res=dic.get(node.prefixSum-targetSum,0)
            
            dic[node.prefixSum]=dic.get(node.prefixSum,0)+1
            
            res+=trav(node.left,targetSum,dic)
            res+=trav(node.right,targetSum,dic)
            
            dic[node.prefixSum]-=1
            
            return res
            
            
        return trav(root,targetSum,dic)