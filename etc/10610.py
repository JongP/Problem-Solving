n=input()

nums = list(n)
nums.sort(reverse=True)

myNum = int("".join(nums))

if myNum%30:
    print(-1)
else:
    print(myNum)