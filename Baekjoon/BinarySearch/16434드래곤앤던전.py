#should be more sophisticated
import math
import sys
input=sys.stdin.readline

N,atk=map(int,input().rstrip().split())
rooms=[]

for _ in range(N):
    rooms.append(list(map(int,input().rstrip().split())))

#get maxHP
maxHP=1
for t,a,h in rooms:
    if t==2: continue
    maxHP+=a*(math.floor(h/atk))


def isSuc(num,atk):
    hCur=num
    aCur=atk
    for t,a,h in rooms:
        if t==1:
            if h<=aCur:
                continue
            elif h%aCur==0:
                hCur-=a*(h//aCur-1)
            else:
                hCur-=a*math.floor(h/aCur)
            if hCur<=0:
                return False
        else:
            hCur+=h
            if hCur>num:
                hCur=num
            aCur+=a
    return True
le=1
ri=maxHP+1
while le<ri:
    mid=(le+ri)//2
    #print(mid)
    if isSuc(mid,atk):
        ri=mid
    else:
        le=mid+1

print(le)


#https://www.acmicpc.net/source/25963353
import sys
n, h_atk = map(int,sys.stdin.readline().split())
h_hp = 0
cur_hp = 0
h_damage =0
info=[]
for _ in range(n):
    info.append(list(map(int,sys.stdin.readline().split())))



for i in info:
    if i[0] == 1:
        atkcnt = i[2]%h_atk
        if atkcnt == 0 :
            h_damage = -(i[1]*(i[2]//h_atk-1))
        else:
            h_damage = -(i[1]*(i[2]//h_atk))       
    else:
        h_atk += i[1]
        h_damage = i[2]
    cur_hp += h_damage
    if cur_hp>0:
        cur_hp = 0
    h_hp = max(h_hp,abs(cur_hp))
    
print(h_hp+1)