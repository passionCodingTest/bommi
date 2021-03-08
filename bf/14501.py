import sys
from itertools import combinations


N=int(sys.stdin.readline())

#여러개 입력 : a,b,c = map(int,sys.stdin.readline().split())
# 한 개 입력 :  int(sys.stdin.readline())
#처음엔 combination으로 푸는 줄 dp강의 들어야겠다. 

t = []
p = []
dp = []
for i in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(N - 1, -1, -1):
    if t[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])



