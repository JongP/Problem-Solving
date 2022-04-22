class Solution:
    def search(self) :

        def calOnes(num):
            res=0
            print(num,bin(num))
            while num:
                num,rem = divmod(num,2)
                res+=rem
            print(res)
            return res


        num_ones=0
        res=0
        for i in range(6,127):
            if num_ones< calOnes(i):
                res=i
                num_ones=calOnes(i)

                    
        return res
sol=Solution()
print(sol.search())
