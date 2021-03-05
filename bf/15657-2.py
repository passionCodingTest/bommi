##약간 더 빠름

n,m=map(int, input().split())
L=list(map(int, input().split()))
array=[]
L.sort()
check=[False]*n

def dfs(x,next):

    if(x==m):
        print(*array)
        return
 
    for i in range (n):
        if check[i]:
            continue
        
        array.append(L[i])

        dfs(x+1,i+1)
        check[i]=True
        array.pop()

        for j in range(i + 1, n):
            check[j] = False
       

dfs(0,0)