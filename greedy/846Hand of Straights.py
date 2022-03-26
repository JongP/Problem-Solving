class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnter=collections.Counter(hand)
        hand=sorted(set(hand))
        hashMap={}
        
        idx=0
        #print(hand)
        while idx<len(hand):
            needed=cnter[hand[idx]]
            
            until=idx+groupSize-1
            hashMap[until]=needed
            
            trav=idx
            
            while trav<=until:
                #print(trav,idx)
                if trav>=len(hand) or hand[trav]-hand[idx]!=trav-idx:
                    return False
                
                if cnter[hand[trav]]<needed:
                    return False
                elif cnter[hand[trav]]>needed:
                    until=trav+groupSize-1
                    hashMap[until]=cnter[hand[trav]]-needed
                    needed=cnter[hand[trav]]
                
                if trav in hashMap:
                    needed-=hashMap[trav]
                
                
                
                trav+=1           
            
            
            
            
            idx=trav
            
        return True
    
    #1 2 3  2 3 4    3
#https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    def isNStraightHand(self, hand, W):
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0