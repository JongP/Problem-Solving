class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=len(s1)
        l2=len(s2)
        
        if l2<l1:
            return
        
        #preprocessing 
        
        myDict= {}
        wordCnt=0
        ansCnt=0
        for char in s1:
            if char not in myDict:
                myDict[char]=1
                ansCnt+=1
            else:
                myDict[char]+=1
        
        #setting sliding window
        le=0
        ri=l1-1
        for i in range(l1):
            if s2[i] in myDict:
                if myDict[s2[i]] == 1:
                    wordCnt+=1
                elif myDict[s2[i]] ==0:
                    wordCnt-=1
                myDict[s2[i]]-=1
                print(s2[i],wordCnt)
        
        if wordCnt==ansCnt:
            return True
        
        
        #moving slide
        le=0
        ri=l1-1
        while ri<l2-1:
            if s2[le] in myDict:
                if myDict[s2[le]]==-1:
                    wordCnt+=1
                elif myDict[s2[le]]==0:
                    wordCnt-=1
                myDict[s2[le]]+=1
                
            if s2[ri+1] in myDict:
                if myDict[s2[ri+1]]==1:
                    wordCnt+=1
                elif myDict[s2[ri+1]]==0:
                    wordCnt-=1
                myDict[s2[ri+1]]-=1
                if wordCnt==ansCnt:
                    return True
            le+=1
            ri+=1
            
        return False
#https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False


    def BestcheckInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Chars = {char: 0  for char in s1}
        s2Chars = {char: 0 for char in s1}
        
        left = 0
        right = len(s1) -1 
        
        for i in s1:
            s1Chars[i] += 1
            
        for i in range(0, len(s1)):
            char = s2[i]
            if char in s2Chars:
                s2Chars[char] += 1
        
        while right < len(s2) - 1:
            if s1Chars == s2Chars:
                return True
            
            l = s2[left]
            if l in s2Chars:
                s2Chars[l] -= 1
            left += 1
            
            right += 1
            r = s2[right]
            if r in s2Chars:
                s2Chars[r] += 1
            
        return s1Chars == s2Chars