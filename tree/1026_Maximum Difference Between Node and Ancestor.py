# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        
        if not root:
            return 0
        
        def getMaxMin(node):
            
            maxN=minN=node.val
            
            for child in [node.left, node.right]:
                if child:
                    cMax,cMin=getMaxMin(child)
                    
                    if self.ans<abs(cMax-node.val):
                        self.ans=abs(cMax-node.val)
                    if self.ans<abs(node.val-cMin):
                        self.ans=abs(node.val-cMin)

                    if cMax>maxN:
                        maxN=cMax
                    if cMin<minN:
                        minN=cMin
                
                
            
            return maxN,minN
        
        getMaxMin(root)
        
        return self.ans

#example fast solution
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # for every node get the max and min node in its left
        # and right subtree and compute the max abs diff
        
        answer=0
        def findDiff(node):
            nonlocal answer
            if not node: return (float('inf'),float('-inf'))
            if not node.left and not node.right: return (node.val, node.val)
            lmn, lmx = findDiff(node.left)
            rmn, rmx = findDiff(node.right)
            answer=max(answer, abs(node.val-min(lmn, rmn)))
            answer=max(answer, abs(node.val-max(lmx, rmx)))
            return min(node.val, lmn, rmn), max(node.val, lmx, rmx)
    
        mn, mx = findDiff(root)
        answer=max(answer, abs(root.val-mn))
        answer=max(answer, abs(root.val-mx))
        #print(root.val, mn, mx, answer)
        
        return answer