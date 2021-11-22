#Delete Tree
#211122 solved 60min

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val==key:
            if not root.right:
                return root.left
            par=None
            trav=root.right
            while trav.left:
                par=trav
                trav=trav.left
            
            if not par:
                trav.left=root.left
                return trav
            par.left=None
            trav.left=root.left
            trav.right=root.right
            return trav
        
        par=None
        trav=root
        leftFlag=True
        while trav and trav.val!=key:
            par=trav
            if key<trav.val:
                leftFlag=True
                trav=trav.left
            else:
                leftFlag=False
                trav=trav.right
        
        
        #no such key:
        if not trav:
            return root
        
        rPar=None
        rTrav=trav.right
        
        #no first right child
        if not rTrav:
            if leftFlag: par.left=trav.left
            else: par.right=trav.left
            return root
        
        while rTrav.left:
            rPar=rTrav
            rTrav=rTrav.left
            
        if leftFlag: par.left=rTrav
        else: par.right=rTrav
        
        rTrav.left=trav.left
        if rPar:
            rPar.left=rTrav.right
            rTrav.right=trav.right
            
        return root