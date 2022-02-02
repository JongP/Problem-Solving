class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def makeDict(p:str) ->dict :
            d={}
            for c in p:
                d[c]=d.get(c,0)+1
                
            return d
        
        if len(s)<len(p):return None
        
        res=[]
        d=makeDict(p)
        cnt=len(p)
        
        #ini
        for i in range(len(p)):
            if s[i] in d: 
                d[s[i]]-=1        
                if d[s[i]]>=0: cnt-=1
                if cnt==0:
                    res.append(0)
        
        for i in range(1,len(s)-len(p)+1):
            if s[i-1] in d:
                d[s[i-1]]+=1
                if d[s[i-1]]>0: cnt+=1
            if s[i+len(p)-1] in d:
                d[s[i+len(p)-1]]-=1
                if d[s[i+len(p)-1]]>=0: cnt-=1
            if cnt==0 : res.append(i)

        
        return res

#https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/175987/Python-solution
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
#examle solution
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = {}   # hash stores the list of characters we need to cross-off. Initially has all of p in it
        for c in p:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        count = len(p)  # number of characters still to be crossed-off
        
        # initialize
        result = []
        left = 0    # the current candidate is s[left:right+1]
        right = 0
        while right < len(s):
            # for every iteration, check if current character is a desired char. if so, cross it off. otherwise, move on to the next character
            if s[right] in hash:
                hash[s[right]] -= 1
                if hash[s[right]] >= 0: # If we have a negative hash value(meaning more than enough of that particular character), it means we are not getting any closer to the solution, so, count should not change
                    count -= 1
            
            
            # print 'left=', left, 'right=', right, 'count=', count, 'hash=', hash, 'cur_window=', s[left:right+1] 
            # if all items are crossed-off, add to result list
            if count == 0:
                result.append(left)
            
            
            # Move window only if the minimum size is met. 
            if right == left + len(p) - 1:   
                if s[left] in hash:     # If the char we are getting rid of is already in the hash, increment the hash (add to the items that we need to cross-off)
                    if hash[s[left]]>=0:    # If the hash (number of items we need to cross-off) is negative(i.e we have had double chars in out current window), do not increment the required count
                        count += 1
                    hash[s[left]] += 1
                left += 1
            right += 1
            
        return result