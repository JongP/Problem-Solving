class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return root
        
        rootCopy= Node(val=root.val)
        root.copy=rootCopy
        
        stk=[root]

        while stk:
            cur=stk.pop()
            curCopy=cur.copy
            
            for ch in cur.children:
                chCopy=Node(val=ch.val)
                ch.copy=chCopy
                
                curCopy.children.append(chCopy)
                
                stk.append(ch)
        
        
        return rootCopy

s#https://leetcode.com/problems/clone-n-ary-tree/discuss/707612/Python-1-Liner
    def cloneTree(self, root: 'Node') -> 'Node':
	    return Node(root.val, [self.cloneTree(child) for child in root.children]) if root else None