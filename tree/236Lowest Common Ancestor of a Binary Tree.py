# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(node) -> 'TreeNode':
            if not node: return None
            
            left=traverse(node.left)
            if left and left!=p and left!=q: return left
            right=traverse(node.right)
            
            if left and right:
                return node
            
            if node==p or node==q: return node
            
            return left or right
            
            
        return traverse(root)

#iterative solution
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None} #you can memorize the parent of each node O(n)
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]