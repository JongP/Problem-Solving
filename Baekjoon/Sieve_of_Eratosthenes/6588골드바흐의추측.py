import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

maxN=1000000
arr=[]
dp=[True]*(maxN+1)

def findGold(num):
    strt=1
    end=len(arr)-1
    while strt<=end:
        sN=arr[strt]+arr[end]
        if sN>num:
            end-=1
        elif sN<num:
            strt+=1
        else:
            print("%d = %d + %d" %(num,arr[strt],arr[end]))
            return
    print("Goldbach's conjecture is wrong.")


for i in range(2,maxN+1):
    if not dp[i]:
        continue
    arr.append(i)
    for j in range(i*i,maxN+1,i):
        dp[j]=False


num=int(input())
while num:
    findGold(num)
    num=int(input())


#https://www.acmicpc.net/source/34214329
import sys
input = sys.stdin.readline
print = sys.stdout.write
MAX = 1000001

def solve():
    # 에라토스테네스의 체
    sieve = [False]*2 + [True]*(MAX-2)
    for i in range(3,int(MAX**0.5),2):
        if sieve[i]:
            sieve[i*2::i] = [False]*((MAX-i-1)//i)

    # 소수 리스트 구하기
    prime = []
    for i in range(3,MAX,2):
        if sieve[i]:
            prime.append(i)

    # 추측 검증
    while True:
        n = int(input())
        if not n:
            break

        for i in prime:
            if sieve[n-i]:
                print("%d = %d + %d\n" %(n,i,n-i))
                break
solve()