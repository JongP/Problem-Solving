class Solution:
    def isPalindrome(self, s: str) -> bool:
        le,ri=0,len(s)-1
        
        while le<ri:       
            while not s[le].isalpha() and not s[le].isdigit() and le<ri : le+=1
            while not s[ri].isalpha() and not s[ri].isdigit() and le<ri : ri-=1
            
            if le!= ri and s[le].lower()!=s[ri].lower():
                return False
            le+=1
            ri-=1
        
        return True