class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat2=list(map(list,zip(*mat2)))
        m,n=len(mat1),len(mat2)

        res=[]
        
        for i in range(m):
            res.append([])
            
            for j in range(n):
                res[-1].append(sum(val1*val2 for val1,val2 in zip(mat1[i],mat2[j])))
            
        
        return res