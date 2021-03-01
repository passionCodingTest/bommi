n,m =map(int, input().split())

num_list=[1+ i for i in range(n)]
check_num=[False]*n

array=[]

def dfs(x):
    if x==m:
        print(*array)
        return

    for i in range(n):
        if check_num[i]:
            continue

        array.append(num_list[i])
        check_num[i]=True

        
        dfs(x+1)

        array.pop()
        check_num[i]=False

dfs(0)
