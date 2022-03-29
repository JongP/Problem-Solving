class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res=[]
        
        hashMap={}
        found=set()
        
        def dfs(node):
            if not node: return "  "
            
            val=dfs(node.left)+" "+dfs(node.right)+" "+str(node.val)
            h=hash(val)
            if h in hashMap and h not in found:
                found.add(h)
                res.append(node)
                
            hashMap[h]=node
            
            return val
        
        dfs(root)
        
        return res