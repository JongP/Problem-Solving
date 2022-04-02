# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        que=deque([(root,0)])
        
        
        #hashMap
        hashMap=defaultdict(list)
        curMin=curMax=0
        while que:
            for _ in range(len(que)):
                node,col=que.popleft()
                
                hashMap[col].append(node.val)
                
                if col>curMax: curMax=col
                if col<curMin: curMin=col
                    
                if node.left:
                    que.append((node.left,col-1))
                    
                if node.right:
                    que.append((node.right,col+1))
        
        
        #res
        res=[]
        for i in range(curMin,curMax+1):
            res.append(hashMap[i])
        return res
        
        