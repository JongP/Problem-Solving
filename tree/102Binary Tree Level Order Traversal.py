# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        que=deque([root])
        res=[]
        
        while que:
            l=len(que)
            tmpL=[]
            for _ in range(l):
                cur=que.popleft()
                tmpL.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
        
            res.append(tmpL)
        
        return res


#https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/1219538/Python-Simple-bfs-explained
class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, result = deque([root]), []
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result
#comment// sNote to myself : range(len(queue)) does not keep changing with every iteration. It is calculated only one time everytime we enter the while loop.