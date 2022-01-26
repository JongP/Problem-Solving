#hint from leetcode
class Solution:
    
    def mergeArray(self,res1,res2) -> List[int]:
        l1,l2=len(res1),len(res2)
        idx1=idx2=0
        res=[]
        
        while idx1<l1 and idx2<l2:
            if res1[idx1] < res2[idx2]:
                res.append(res1[idx1])
                idx1+=1
            else:
                res.append(res2[idx2])
                idx2+=1
        
        if idx2<l2: idx1,l1,res1=idx2,l2,res2
        while idx1<l1:
            res.append(res1[idx1])
            idx1+=1
        return res
    
    def getElements(self,root) -> List[int]:
        stk=[]
        trav=root
        res=[]
        
        while stk or trav:
            while trav:
                stk.append(trav)
                trav=trav.left
            
            trav=stk.pop()
            res.append(trav.val)
            
            trav=trav.right
        
        
        return res
        
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1=self.getElements(root1)
        res2=self.getElements(root2)
        res= self.mergeArray(res1,res2)
        
        return res