class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res=0
        idx=0
        
        while idx<len(seats) and seats[idx]==0: 
            idx+=1
            res+=1
            
        tmp=0
        while idx<len(seats):
            if seats[idx]==0:
                tmp+=1
            else:
                if res<math.ceil(tmp/2):#if u use res=max(res,math.ceil(tmp/2)), it takes a lot of times. 
                    res=math.ceil(tmp/2)
                tmp=0
            
            
            idx+=1
            
        res=max(res,tmp)
            
            
        return res
#https://leetcode.com/problems/maximize-distance-to-closest-person/discuss/137912/JavaC%2B%2BPython-One-pass-Easy-Understood
#I don't need tmp. we just follow the index
    def maxDistToClosest(self, seats):
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        return max(res, n - last - 1)