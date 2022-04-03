class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        newinterval [c,d]
        #1 (c) (d)  [a, (c) b](c) (d) 
        res=[]
        
        for interval in intervals:
            res[-1]
            res.append(interval)
        
        
        """
        A,B= newInterval
        
        res=[]
        idx=0
        #preprocessing
        while idx<len(intervals):
            s,e=intervals[idx]
            if e<A:
                res.append(intervals[idx])
            else:
                break
            idx+=1
        
        res.append(newInterval)
        #merge
        while idx<len(intervals):
            #can not affet
            if res[-1][1]<intervals[idx][0]:
                res.append(intervals[idx])
            #can affect --> merge
            else:
                s,e=res.pop()
                res.append([min(s,intervals[idx][0]),max(e,intervals[idx][1])  ])
            
        
            idx+=1
            
            
        
        
        return res


#https://leetcode.com/problems/insert-interval/discuss/844494/Python-O(n)-solution-explained
class Solution:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return res + [I] + intervals[i+1:]