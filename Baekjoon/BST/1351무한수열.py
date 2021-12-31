from math import floor
import sys
input=sys.stdin.readline

n,p,q= map(int,input().split())

dic={0:1}


def helper(num):
    if num in dic:
        return dic[num]
    dic[num]=helper(num//p)+helper(num//q)
    return dic[num]

print(helper(n))