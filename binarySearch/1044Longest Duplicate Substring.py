#hint on related topic
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        le,ri,ret,retIndex=0,len(s)-1,0,0
        
        while le<=ri:
            mid=(le+ri+1)//2
            
            val=self.isDup(s,mid)
            
            if val!=-1:
                ret=mid
                retIndex=val
                le=mid+1
            else:
                ri=mid-1
            
             
        return s[retIndex:retIndex+ret]
            
            
    def isDup(self,s,n):
        visited=set()
        for i in range(len(s)-n+1):
            tmp=hash(s[i:i+n])
            if tmp in visited:
                return i
            visited.add(tmp)
        
        return -1
            
#fist tried trie w/ o(n^2) --> TLE. how to reduce O(n)


#Rabin Karp Algorithm
#https://leetcode.com/problems/longest-duplicate-substring/discuss/695029/Python-Binary-search-O(n-log-n)-average-with-Rabin-Karp-explained
class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h, t, d = (1<<(8*M-8))%q, 0, 256

        dic = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            for j in dic[t]:
                if text[i+1:i+M+1] == text[j:j+M]:
                    return (True, text[j:j+M])
            dic[t].append(i+1)
        return (False, "")

    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found