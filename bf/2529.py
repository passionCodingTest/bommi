#https://hjp845.tistory.com/128
#조건을 분류해주는 함수를 만드는 습관을 들여야 겠다. 

num = int(input())
op = input().split()
check = [False] * 10
mx , mn = "",""

def poss(i,j,k): # 부등호 조건이  만족할 때만 작동
    if k == ">":
        return i>j
    else:
        return i<j


def recu(cnt, s):
    global mx,mn
    if cnt > num: #맨처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return
    for i in range(10): #재귀 함수
        if check[i] == False:
            if cnt == 0 or poss(s[-1],str(i),op[cnt-1]):
                check[i] = True
                recu(cnt+1,s+str(i))
                check[i] = False

recu(0,"")
print(mx)
print(mn)