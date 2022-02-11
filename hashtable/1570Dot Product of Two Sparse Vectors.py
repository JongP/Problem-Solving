#two pointer
#quite slow
class SparseVector:
    def __init__(self, nums: List[int]):
        self.data=[]
        for i,v in enumerate(nums):
            if v==0:
                continue
            self.data.append((i,v))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        idx1=idx2=0
        res=0
        
        while idx1<len(self.data) and idx2<len(vec.data):
            i1,v1=self.data[idx1]
            i2,v2=vec.data[idx2]
            
            if i1==i2:
                res+=v1*v2
                idx1+=1
                idx2+=1
            elif i1<i2:
                idx1+=1
            else:
                idx2+=1
                
        
        
        return res


#hashTable
#better than above
class SparseVector:
    def __init__(self, nums: List[int]):
        self.data={}
        for i,v in enumerate(nums):
            if v==0:
                continue
            self.data[i]=v
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for idx in self.data:
            if idx not in vec.data: continue
            res+=self.data[idx]*vec.data[idx]
        return res        

#https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/825936/Python-dictionary
#pythonic
class SparseVector:
	def __init__(self, A: List[int]):
		self.m = {i: x for i, x in enumerate(A) if x}
	def dotProduct(self, other: 'SparseVector') -> int:
		return sum([x * y for i, x in self.m.items() for j, y in other.m.items() if i == j])
        
