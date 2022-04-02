from collections import defaultdict,Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #1,2,3 4, 4,5,6
        #hashMap  --> deque()   [3,2] 
        #for num in  nums
        # hashMap[num-1]? o--> connect (num-1,num,) 
        #   val=hashMap[num-1].pop(). hashMap[num].append(val)
        #                 x--> don't connect. create new series
        
        #varify True/False. can iterate whole hashMap. O(n)
        
        #1 build hashMap
        hashMap=defaultdict(list)
        fullSeq=Counter()
        cnt=0
        
        for num in nums:
            if len(hashMap[num-1])!=0:
                val=hashMap[num-1].pop()
                if val==2:
                    cnt-=1
                    fullSeq[num]+=1
                else:
                    hashMap[num].append(val+1)
                    
            elif fullSeq[num-1]>0:
                fullSeq[num-1]-=1
                fullSeq[num]+=1

            else:
                hashMap[num].append(1)
                cnt+=1
        
        
        
        #2 varify
        return cnt==0
                
        
#https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution        
def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True