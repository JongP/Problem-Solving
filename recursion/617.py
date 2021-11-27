# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        
        
        def goDFS(node,node1,node2):
            if not node:
                return
            
            if not node1.left or not node2.left:
                node.left = node1.left or node2.left
            else:
                node.left=TreeNode(val=node1.left.val+node2.left.val)
                goDFS(node.left,node1.left,node2.left)
            
            if not node1.right or not node2.right:
                node.right = node1.right or node2.right
            else:
                node.right=TreeNode(val=node1.right.val+node2.right.val)
                goDFS(node.right, node1.right,node2.right)
            
            
        
        
        
        root=TreeNode(val=root1.val+root2.val)
        
        goDFS(root,root1,root2)
        
        return root
#https://leetcode.com/problems/merge-two-binary-trees/discuss/159138/Python-solution
    def zitaoMergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t1 == None:
            return t2
        elif t2 == None:
            return t1
        new_root = TreeNode(t1.val + t2.val)
        left = self.mergeTrees(t1.left, t2.left)
        right = self.mergeTrees(t1.right, t2.right)
        new_root.left = left
        new_root.right = right
        return new_root