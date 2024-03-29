# 1086: 박성원
# https://www.acmicpc.net/problem/1086
# https://ca.ramel.be/147
# pypy 통과


import sys
from math import gcd, factorial

n = int(sys.stdin.readline())
stack = [] 
for _ in range(n):
    stack.append(int(sys.stdin.readline()))
long=[]
for i in stack:
    long.append(len(str(i)))
k=int(sys.stdin.readline())
dp=[[-1]*k for _ in range(1<<n)]
rm=[[-1]*(sum(long)) for _ in range(n)]
for i in range(n):
    for j in range(sum(long)):
        rm[i][j]=(stack[i]*10**j)%k 


def dfs(L, visited, rest):
    if visited==(1<<n)-1:
        if rest==0:
            return 1
        else:
            return 0
    if dp[visited][rest]!=-1:
        return dp[visited][rest]
    for i in range(n):
        if visited & (1<<i)==0:
            dp[visited][rest]+=dfs(L+long[i], visited|(1<<i), (rest+rm[i][L])%k )
    dp[visited][rest]+=1
    return dp[visited][rest]

temp=dfs(0,0,0)
F=factorial(n)
if temp==0:
    print('0/1')
else:
    v=gcd(F,dp[0][0])
    print('{}/{}'.format(temp//v,F//v))