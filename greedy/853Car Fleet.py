class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cur=-1
        res=0
        
        cars=sorted([ (p,(target-p)/s)  for p,s in zip(position,speed) ], reverse=True )
        
        for _, t in cars:
            if cur<t:
                cur=t
                res+=1
            
        return res

#https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward
    def carFleet(self, target, pos, speed):
        time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res