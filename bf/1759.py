import sys
from itertools import combinations

dict = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, sys.stdin.readline().split())
pwd = sorted(list(map(str, sys.stdin.readline().split())))
print(pwd)
# 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations, combinations을 사용
# 두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product를 사용
#from itertools import product
#from itertools import permutations
#from itertools import combinations

comb = combinations(pwd, L)

for c in comb:
    count = 0
    for letter in c:
        if letter in dict: #최소 1개의 모음 2개의 자음
            count += 1

    if (count >= 1) and (count <= L-2):
        print(''.join(c))