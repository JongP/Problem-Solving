class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que=collections.deque([(root,1)])
        res=1
        
        while que:
            left,right=math.inf,-math.inf
            for _ in range(len(que)):
                cur,index = que.popleft()
                
                if index<left: left=index
                if index>right: right=index
                
                if cur.left:
                    que.append((cur.left,index*2))
                if cur.right:
                    que.append((cur.right,index*2+1))
            
            if res<right-left+1:
                res=right-left+1
        
        return res

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que=collections.deque([(root,1)])
        res=1
        
        while que:

            
            if res<que[-1][1]-que[0][1]+1:
                res=que[-1][1]-que[0][1]+1

            
            for _ in range(len(que)):
                cur,index = que.popleft()
                
                
                if cur.left:
                    que.append((cur.left,index*2))
                if cur.right:
                    que.append((cur.right,index*2+1))

        
        return res