n,m =map(int, input().split())
L=list(map(int, input().split()))
L.sort()
check=[False]*n
array=[]

def dfs(x):

    if(x==m):
        print(*array)
        return
  
    for i in range (n):
        if not check[i]:
            
            array.append(L[i])
            dfs(x+1)

            array.pop()
            check[i]=False
            
            
    
dfs(0)