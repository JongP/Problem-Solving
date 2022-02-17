class Solution:
    def validPalindrome(self, s: str) -> bool:
        string=s
        s=0;e=len(string)-1
        
        def isPal(string,s,e):
            while s<e:
                if string[s]!=string[e]: return False
                s+=1;e-=1;
            return True
        
        
        while s<e:
            if string[s]!=string[e]:
                if isPal(string,s+1,e): return True
                if isPal(string,s,e-1): return True
                return False
                
            s+=1;e-=1;
        
        
        
        return True
    

#https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

#https://leetcode.com/problems/valid-palindrome-ii/discuss/107720/C%2B%2BJavaPython-Easy-and-Concise
def validPalindrome(self, s):
        i = 0
        while i < len(s) / 2 and s[i] == s[-(i + 1)]: i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]