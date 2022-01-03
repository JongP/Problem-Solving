class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #1->3 2->3 3->1
        if n==1:
            return 1
        
        cnt=[0]*n
        check=set()
        cand=set()
        for a,b in trust:
            a-=1;b-=1;
            cnt[b]+=1
            if cnt[b]==n-1:
                cand.add(b)
            check.add(a)
            
        for i in cand:
            if  i not in check:
                return i+1
            
        return -1