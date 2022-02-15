# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #O(n), O(height of tree)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=-1001
        
        def helper(node):     
            if not node:
                return -1001
            
            leftVal=helper(node.left)
            rightVal=helper(node.right)
            
            curSum=max(node.val,node.val+max(leftVal,rightVal))
            
            if curSum > self.res: 
                self.res=curSum
            if node.val+ leftVal+rightVal > self.res: 
                self.res=node.val+rightVal+leftVal
            
            return curSum
            
        
        
        helper(root)
        
        return self.res
    #https://devbruce.github.io/python/py-13-global,nonlocal/


#https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
class Solution:
     def maxPathSum(self, root: TreeNode) -> int:
 	    max_path = float("-inf") # placeholder to be updated
 	    def get_max_gain(node):
 			nonlocal max_path # This tells that max_path is not a local variable
 			if node is None:
 				return 0
 				
 			gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observations
 		    gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
 			
 		    current_max_path = node.val + gain_on_left + gain_on_right # Read first three images of going down the recursion stack
 		    max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
 			
 		    return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack
 			
 			
 	get_max_gain(root) # Starts the recursion chain
 	return max_path		