#557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        le=0
        ri=0
        l=len(s)
        lastFlag=False
        answer=""
        while le<l:
            
            while ri<l and  s[ri]!=' ':
                ri+=1
            if ri!=l-1:
                ri-=1
            
            while le<=ri:
                answer+=s[ri]
                ri-=1
                
            while le<l and s[le]!=' ':
                le+=1
            
            if le==l:
                break
                
            answer+=" "
            
            le+=1
            ri=le
        return answer

    def shortReverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[::-1] for w in s.split()])