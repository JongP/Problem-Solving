#greedy+BFS
#hard coding
from collections import deque,defaultdict
n,k=map(int,input().split())
m=len(str(n))
que=deque()
arr=[ n//(10**i)-10*(n//(10**(i+1)))   for i in range(m-1,-1,-1)]


if len(arr)==1:
    print(-1)
    exit()
if len(set(arr))!=len(arr):
    flag=True
else: flag=False

def arrToNum(arr):
    num=0
    arr.reverse()
    for i in range(len(arr)):
        num+=arr[i]*(10**i)
    return num

def findIndexMax(arr,m,l):
    tmpIs=[]
    for i in range(len(arr)-l,len(arr)):
        if arr[i]==m:
            tmpIs.append(i)
    return tmpIs


maxList=[]
que.append((arr,m,k))

while que:
    ar,level,leftK=que.popleft()
    
    if leftK==0:
        maxList.append(arrToNum(ar))
        continue
    if level==0:
        continue
    tmpMax=max(ar[-1*level:])
    
    if tmpMax==ar[-1*level]:
        que.append((ar,level-1,leftK))
        continue

    tmpIs=findIndexMax(ar,tmpMax,level)
    for tmpI in tmpIs:
        tmpAr=ar.copy()
        tmpAr[-1*level],tmpAr[tmpI]=tmpAr[tmpI],tmpAr[-1*level]
        que.append((tmpAr,level-1,leftK-1))

if maxList:
    print(max(maxList))
elif flag:
    print(arrToNum(ar))
elif ar[1]==0:
    print(-1)
elif leftK%2==0:
    print(arrToNum(ar))
else:
    ar[-1],ar[-2]=ar[-2],ar[-1]
    print(arrToNum(ar))
#print(ar, leftK)

#52676 2 76652
#2133 2 3321




#only bfs no greedy
#include<iostream>
#include<algorithm>
#include<queue>
#include<string>
#include<set>
#include<vector>
 
#define endl "\n"
#define MAX 1000000 + 1


using namespace std;
 
string Inp;
int K, M;
vector<int> Answer;
 
int Invert(string S)
{
    int Sum = 0;
    for (int i = 0; i < S.length(); i++)
    {
        Sum = Sum + (S[i] - '0');
        if (i != S.length() - 1) Sum = Sum * 10;
    }
    return Sum;
}
 
void Input()
{
    cin >> Inp >> K;
    M = Inp.length();
 
    if (M == 1 || (M == 2 && Invert(Inp) % 10 == 0))
    {
        cout << "-1" << endl;
        exit(0);
    }
}
 
void BFS(string S)
{
    queue<string> Q;
    Q.push(S);
    int Cur_K = 0;
    int Max = 0;
 
    while (Q.empty() == 0 && Cur_K < K)
    {
        int Qs = Q.size();
        set<string> Visit;
 
        for (int q = 0; q < Qs; q++)
        {
            string Cur = Q.front();
            Q.pop();
 
            for (int i = 0; i < M - 1; i++)
            {
                for (int j = i + 1; j < M; j++)
                {
                    if (i == 0 && Cur[j] == '0') continue;
 
                    swap(Cur[i], Cur[j]);
                    if (Visit.find(Cur) == Visit.end())
                    {
                        if (Cur_K == K - 1 && Max < Invert(Cur))
                        {
                            Max = Invert(Cur);
                        }
                        Q.push(Cur);
                        Visit.insert(Cur);
                    }
                    swap(Cur[i], Cur[j]);
                }
            }
        }
        Cur_K++;
    }
 
    if (Cur_K != K) cout << "-1" << endl;
    else cout << Max << endl;
 
}
 
void Solution()
{
    BFS(Inp);
}
 
void Solve()
{
    Input();
    Solution();
}
 
int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    //freopen("Input.txt", "r", stdin);
    Solve();
 
    return 0;
}


#출처: https://yabmoons.tistory.com/152 [얍문's Coding World..]