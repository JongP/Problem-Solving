class MyCounter:
    def __init__(self,t):
        self.c=collections.Counter(t)
        self.l=len(self.c)#양수 갯수
        
    def insert(self,ch):
        if ch not in self.c: return self.l==0
        
        if self.c[ch]==1: self.l-=1
        self.c[ch]-=1
        
        return self.l==0
    
    def delete(self,ch):
        if ch not in self.c: return self.l==0
        
        self.c[ch]+=1
        if self.c[ch]==1: self.l+=1
        
        return self.l==0
        
    def print(self):
        print(self.c)
        print(self.l)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n=len(s),len(t)
        
        counter=MyCounter(t)
        
        res=""
        
        le=0
        for ri in range(len(s)):
            
            if counter.insert(s[ri]):
                while le<=ri:
                    if not counter.delete(s[le]): 
                        if not res or len(res)>(ri-le+1):
                            res=s[le:ri+1]
                        le+=1
                        break
                    le+=1
        
            #print(counter.print())
        
        return res

#https://leetcode.com/problems/minimum-window-substring/discuss/226911/Python-two-pointer-sliding-window-with-explanation
#similiar solution
    def found_target(target_len):
        return target_len == 0

    class Solution(object):
        def minWindow(self, search_string, target):
            """
            :type s: str
            :type t: str
            :rtype: str
            """
            target_letter_counts = collections.Counter(target)
            start = 0
            end = 0
            min_window = ""
            target_len = len(target)        
            
            for end in range(len(search_string)):
                # If we see a target letter, decrease the total target letter count
                if target_letter_counts[search_string[end]] > 0:
                    target_len -= 1

                # Decrease the letter count for the current letter
                # If the letter is not a target letter, the count just becomes -ve
                target_letter_counts[search_string[end]] -= 1
                
                # If all letters in the target are found:
                while found_target(target_len):
                    window_len = end - start + 1
                    if not min_window or window_len < len(min_window):
                        # Note the new minimum window
                        min_window = search_string[start : end + 1]
                        
                    # Increase the letter count of the current letter
                    target_letter_counts[search_string[start]] += 1
                    
                    # If all target letters have been seen and now, a target letter is seen with count > 0
                    # Increase the target length to be found. This will break out of the loop
                    if target_letter_counts[search_string[start]] > 0:
                        target_len += 1
                        
                    start+=1
                    
            return min_window


#https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    