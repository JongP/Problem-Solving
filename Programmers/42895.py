from itertools import combinations
#https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    if(N==number) :
        return 1

    numbers=[[]]
    
    numbers.append([N])
    for i in range(2,9):
        new_nums=set([int(str(N)*i)])
        for j in range(1,i//2+1):
            for a in numbers[j]:
                #print(i,j,a)
                for b in numbers[i-j]:
                    new_nums.add(a+b)
                    new_nums.add(a-b)
                    new_nums.add(b-a)
                    new_nums.add(b*a)
                    if a!=0:
                        new_nums.add(b/a)
                    if b!=0:
                        new_nums.add(a/b)
        new_nums.discard(0)
        numbers.append(list(new_nums))
        #print(numbers)
        if number in new_nums:
            return i
        
        
    return -1