class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy=TreeNode(left=root)
        prev=dummy
        trav=root
        left=True
        
        while trav:
            if trav.val>val:
                prev=trav
                trav=trav.left
                left=True
            else:
                prev=trav
                trav=trav.right
                left=False
                
        
        if left:
            prev.left=TreeNode(val=val)
        else:
            prev.right=TreeNode(val=val)
            
        return dummy.left