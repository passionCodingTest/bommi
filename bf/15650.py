n,m =map(int, input().split())

num_list=[1+ i for i in range(n)]

check=[False]*n

array=[]

def dfs(x):
    if (x==m):
        print(*array)
        return

    for i in range (n):
        if check[i]:
            continue

        
        check[i]=True
        print(check)
        array.append(num_list[i])
        dfs(x+1)
        array.pop()

        for j in range(i+1,n):
            #print(j)
            check[j]=False

dfs(0)

    

