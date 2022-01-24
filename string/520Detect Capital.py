class Solution:
    #O(n) O(1)
    def detectCapitalUse(self, word: str) -> bool:

        def isLowercase(ch):
            return ord('a')<=ord(ch)<=ord('z')
        
        lF=uF=sF=False
    
        for i in range(len(word)):
            ch=word[i]
            if isLowercase(ch):
                if uF:
                    if not sF and i!=1:
                        return False
                    else:
                        sF=True
                lF=True
            else:
                if lF:
                    return False
                uF=True
        
        
        
        return True


#example solution
    def detectCapitalUse(self, word: str) -> bool:
#         Correct when num_capitals == 0, 1 (at beginning) or len(word)
        len_word = 0
        num_capitals = 0
        for ch in word:
            if ch == ch.upper():
                num_capitals += 1
            len_word += 1
        if num_capitals == 0 or num_capitals == len_word:
            return True
        elif num_capitals == 1 and word[0].upper() == word[0]:
            return True
        return False