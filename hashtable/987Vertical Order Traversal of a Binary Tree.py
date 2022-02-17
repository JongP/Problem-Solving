from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        hashMap=defaultdict(list)
        que=deque([(root,0)])
        minVal=0
        
        #bfs
        while que:
            tmpHash=defaultdict(list)
            
            for _ in range(len(que)):
                cur,col=que.popleft()
                if col<minVal: minVal=col
                
                if cur.left: que.append((cur.left,col-1))
                if cur.right: que.append((cur.right,col+1))
                
                tmpHash[col].append(cur.val)
                
            for idx, lst in tmpHash.items():
                hashMap[idx].extend(sorted(lst))
        
        #res
        res=[]
        while minVal in hashMap:
            res.append(hashMap[minVal])
            minVal+=1
        
        
        return res

#leetcode solution

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def BFS(root):
            nonlocal min_column, max_column
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    min_column = min(min_column, column)
                    max_column = max(max_column, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). BFS traversal
        BFS(root)

        # step 2). extract the values from the columnTable
        ret = []
        for col in range(min_column, max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret