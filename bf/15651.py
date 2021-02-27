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

        
        #check[i]=True
        array.append(num_list[i])

        dfs(x+1)

        print("array pop 전" , *array)
        array.pop()

        print("array pop 후" , *array)

dfs(0)

    

