class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor=self.getAncestor(root,startValue,destValue)
        
        #print(ancestor.val,self.height)
        
        res=["U" for _ in range(self.height)]
        
        
        def dfs(node,path):
            if not node: return False
            if node.val==destValue:
                return True
            
            path.append("L")
            if dfs(node.left,path):
                return True
            path.pop()
            
            path.append("R")
            if dfs(node.right,path):
                return True
            path.pop()
            
            return False
        
        
        
        dfs(ancestor,res)
    
    
        return "".join(res)
    
    def getAncestor(self,root,startValue,destValue):
        
        def dfs(node,depth):
            if not node:
                return None,False,False
            
            sFlag = node.val==startValue
            if sFlag: self.sDepth=depth
            dFlag = node.val==destValue
            
            
            
            lAnc,lSFlag,lDFlag = dfs(node.left,depth+1)
            if lAnc: return lAnc, True, True
            
            rAnc,rSFlag,rDFlag = dfs(node.right,depth+1)
            if rAnc: return rAnc,True, True
            
            
            sFlag = sFlag or lSFlag or rSFlag
            dFlag = dFlag or lDFlag or rDFlag
            
            anc=None
            if sFlag and dFlag:
                self.height=self.sDepth - depth    
                anc=node
                
            return anc,sFlag,dFlag
            
            
            
        return dfs(root,0)[0] 
            
            
            
#https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root) # only this sub-tree matters
        
        ps = pd = ""
        stack = [(root, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U"*len(ps) + pd


#Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.getPaths(root,startValue,destValue)
        
        print(self.sPath,self.dPath)
        
        idx=0
        while idx<len(self.sPath) and  idx<len(self.dPath) and self.sPath[idx]==self.dPath[idx]: idx+=1
        
        
        res=["U" for _ in range(len(self.sPath)-idx)]
        
        for i in range(idx,len(self.dPath)):
            res.append(self.dPath[i])
            
        return "".join(res)
        
        
        
    def getPaths(self,root,startValue,destValue):
        
        def dfs(node,path):
            if not node: return
            
            if node.val==startValue:
                self.sPath=path.copy()
            elif node.val==destValue:
                self.dPath=path.copy()

            
            path.append("L")
            dfs(node.left,path)
            path.pop()
            
            path.append("R")
            dfs(node.right,path)
            path.pop()
            
            
        dfs(root,[])