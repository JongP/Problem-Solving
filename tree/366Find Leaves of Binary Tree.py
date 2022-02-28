class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[[]]
        
        def dfs(node):
            if not node:
                return -math.inf
            
            if not node.left and not node.right:
                res[0].append(node.val)
                return 0
            
            
            val=max(dfs(node.right),dfs(node.left))+1
            
            while len(res)<val+1: res.append([])
                
            res[val].append(node.val)
            
            
            
            return val
        
        dfs(root)
        
        return res

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[[]]
        
        def dfs(node):
            if not node:
                return -1
            
            
            val=max(dfs(node.right),dfs(node.left))+1
            
            while len(res)<val+1: res.append([])
                
            res[val].append(node.val)
            
            return val
        
        dfs(root)
        
        return res