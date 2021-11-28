"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
          
        if not root:
            return root
        h=1
        trav=root
        while trav.right:
            trav=trav.right
            h+=1
        print(h)
        
        ary=[None]*h
      
        
        def goDFS(node,depth,ary):
            node.next=ary[depth]
            
            if not node.right:
                return
            
            goDFS(node.right,depth+1,ary)
            ary[depth+1]=node.right
            
            goDFS(node.left,depth+1,ary)
            ary[depth+1]=node.left
        
        goDFS(root,0,ary)
        
        
        return root
#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/166296/Python-solution
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def trav(root):
            if not root.left and not root.right:
                return
            if not root.next:
                root.left.next = root.right
                root.right.next = None
            else:
                root.left.next = root.right
                root.right.next = root.next.left
            trav(root.left)
            trav(root.right)
        if not root:
            return
        root.next = None
        trav(root)

    def connect(self, root):
        if not root:
            return 
        root.next = None
        trav = root
        while trav.left:
            head = trav.left
            while trav:
                if not trav.next:
                    trav.left.next = trav.right
                    trav.right.next = None
                    trav = head
                    break
                else:
                    trav.left.next = trav.right
                    trav.right.next = trav.next.left
                    trav = trav.next
    def connect(self, root):
        dic = {}#using dict not ary, u don't need to know height
        def dfs(r, dep):
            if not r:
                return
            if dep in dic:#left first, unlike my solution
                dic[dep].next = r
            r.next = None
            dic[dep] = r
            dfs(r.left, dep + 1)
            dfs(r.right, dep + 1)
        dfs(root, 0)