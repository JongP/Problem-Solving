#revrse sting
#can implement reverse with two pointer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        le=0
        ri=len(s)-1
        
        while le<ri:
            s[le],s[ri]=s[ri],s[le]
            le+=1
            ri-=1