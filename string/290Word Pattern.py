class Solution:
    #O(n), O(n) --> plz check the ref
    #O(k'), O(k) --> k for total length of all words, k for total lenght of distinct words
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        dic={}
        visited=set()
        
        if len(s)!=len(pattern): return False
        
        for i in range(len(s)):
            if pattern[i] not in dic:
                if s[i] in visited:
                    return False
                dic[pattern[i]]=s[i]
                visited.add(s[i])
            elif dic[pattern[i]]!=s[i]:
                return False
            
        return True
        
#https://leetcode.com/problems/word-pattern/discuss/833961/Python-2-hash-tables-explained
#Complexity: time complexity is O(n + m), where n is number of symbols in pattern and m is total number of symbols in s. Space complexity is O(k), where k is total length of all unique words.
class Solution:
    def wordPattern(self, pattern, s):
        d_symb, d_word, words = {}, {}, s.split()
        if len(words) != len(pattern): return False
        for symb, word in zip(pattern, words):
            if symb not in d_symb:
                if word in d_word: return False
                else:
                    d_symb[symb] = word
                    d_word[word] = symb
            elif d_symb[symb] != word: return False
        return True