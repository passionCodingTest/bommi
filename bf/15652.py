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
           
        array.append(num_list[i]) #num_list 0


        # print("array pop 전" , *array)

        dfs(x+1)
        check[i]=True
        array.pop()
        # print("array pop 후" , *array)  

        for j in range(i + 1, n):
            check[j] = False
           

dfs(0)

    

