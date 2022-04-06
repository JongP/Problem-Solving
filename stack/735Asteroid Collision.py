class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        
        for a in asteroids:
            if a<0:
                while stk and stk[-1]>0 and stk[-1]<-a:
                    stk.pop()
                    
                if not stk or stk[-1]<0:
                    stk.append(a)
                elif stk[-1]==-a:
                    stk.pop()
                
                
            else:
                stk.append(a)

        return stk


#https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation
class Solution(object):
    def asteroidCollision(self, asteroids):
        res = []
        for asteroid in asteroids:
            # We only need to resolve collisions under the following conditions:
            # - stack is non-empty
            # - current asteroid is -ve
            # - top of the stack is +ve
            while len(res) and asteroid < 0 and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid: 
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid 
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the 
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
        return res