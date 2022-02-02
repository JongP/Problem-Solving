class Solution:
    #O(n*k*log(k))  --> can be optimized
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=0
        dct={}
        res=[]
        

        for st in strs:
            tmp="".join(sorted(list(st)))
            
            
            if tmp not in dct:
                dct[tmp]=l
                l+=1
                res.append([])
                
            res[dct[tmp]].append(st)
        
        
        return res
        

#https://leetcode.com/problems/group-anagrams/discuss/1398888/C%2B%2BPython-Group-by-sorted-string-group-by-count-characters-Solutions-Clean-and-Concise
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return groups.values()

#counting sort
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(s):
            cnt = [0] * 26
            for c in s: cnt[ord(c) - ord('a')] += 1
            ans = []
            for i in range(26): ans.append(cnt[i] * chr(i + ord('a')))
            return "".join(ans)

        groups = defaultdict(list)
        for s in strs:
            groups[getKey(s)].append(s)
        return groups.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(s):
            cnt = [0] * 26
            for c in s: cnt[ord(c) - ord('a')] += 1
            return tuple(cnt)

        groups = defaultdict(list)
        for s in strs:
            groups[getKey(s)].append(s)
        return groups.values()