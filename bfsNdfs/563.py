class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def goDFS(node) -> tuple:
            global ans

            if not node.left and not node.right:
                node.val=0
                return (0,0)
            
            
            leftSum=0
            rightSum=0
            if node.left:
                leftSum=node.left.val
                le1,ri1=goDFS(node.left)
                leftSum+=le1+ri1
            if node.right:
                rightSum=node.right.val
                le2,ri2=goDFS(node.right)
                rightSum+=le2+ri2           
            node.val=abs(leftSum-rightSum)
            ans+=node.val
            return leftSum,rightSum
                
        
        if root:
            le,ri=goDFS(root)
        
        return ans 
#https://leetcode.com/problems/binary-tree-tilt/discuss/102369/Python-straightforward-solution
def findTilt(self, root):
        def tilt(root):
            # return (sum, tilt) of tree
            if not root: return (0, 0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, abs(left[0] - right[0]) + left[1] + right[1])
        return tilt(root)[1]

    def findTilt(self, root):
        
        def dfs(root):  # get sum of all vals
            if not root:
                return 0
            
            left = dfs(root.left)
            right= dfs(root.right)
            self.tilt += abs(left - right)
            
            return root.val + left + right
        
        self.tilt = 0
        dfs(root)
        return self.tilt