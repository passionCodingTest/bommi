n,m =map(int, input().split())
L=list(map(int, input().split()))
L.sort()
check=[False]*n
array=[]

def dfs(x,next):

    if(x==m):
        print(*array)
        return
    
    for i in range (next,n):
        if not check[i]:
            check[i]=True
            array.append(L[i])
            dfs(x+1,i+1)
            array.pop()
            check[i]=False

dfs(0,0)