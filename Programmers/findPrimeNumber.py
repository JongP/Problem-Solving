from itertools import permutations

def isPrime(num):
    if num ==0 or num ==1: 
        return False
    
    for i in range(2,(num-1)//2+1):
        if num%i ==0 :
            return False
        
    return True

def solution(numbers):
    l = len(numbers)
    num_nodes = set()

    for i in range(1,l+1):
        for per in permutations(numbers,i):
            print(per)
            number=""
            for num in per:
                number+=num

            if  int(number) not in num_nodes and isPrime(int(number)):
                num_nodes.add(int(number))
    print(num_nodes)
    return len(num_nodes)

print(solution("125135"))