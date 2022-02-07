class Solution:
#2 more optimal solution through depp observation
    def uniqueLetterString(self, s: str) -> int:
        ques=[[-1] for _ in range(26)]
        
        for i,c in enumerate(s):
            code=ord(c)-ord('A')
            ques[code].append(i)
        
        for i in range(26): ques[i].append(len(s))
        
        res=0
        for que in ques:
            if len(que)==2: continue
            
            for i in range(1,len(que)-1):
                res+=(que[i]-que[i-1])*(que[i+1]-que[i])
            
            
        return res

#3 further optimzation
    def uniqueLetterString(self, s: str) -> int:
        ques={}
        
        for i,c in enumerate(s):
            if c not in ques: ques[c]=[-1]
            ques[c].append(i)
        
        for k in ques: ques[k].append(len(s))
        
        res=0
        for k in ques:
            que=ques[k]
            if len(que)==2: continue
            
            for i in range(1,len(que)-1):
                res+=(que[i]-que[i-1])*(que[i+1]-que[i])
            
            
        return res
    
#1 poorly sovled at first time
#O(26n)
    def uniqueLetterString(self, s: str) -> int:
        index=[-1]*26
        prev=[-1]*26
        res=0
        
        for i,c in enumerate(s):
            code=ord(c)-ord('A')
            
            prev[code]=index[code]
            index[code]=i
            for j in range(26):
                if index[j]==-1: continue
                res+=index[j]-prev[j]

            
            
            
        return res


#https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)
#how to get intuition
    def uniqueLetterString(self, S):
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)