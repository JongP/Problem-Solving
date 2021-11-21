#21.11.21
#unsolved
#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/1588887/Python-Arriving-at-an-O(N)-solution
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0:
            return None
        
        val=postorder[-1]
        idx=inorder.index(val)
        
        leftIn=inorder[:idx]
        rigthIn=inorder[idx+1:]
        
        
        leftPo=postorder[:idx]
        rightPo=postorder[idx:-1]
            
        
        return TreeNode(val,self.buildTree(leftIn,leftPo),self.buildTree(rigthIn,rightPo))