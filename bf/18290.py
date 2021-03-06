#보류

import sys
data = []

sum_all=0
n,m,k = map(int,sys.stdin.readline().split())
check = [[False for _ in range(m)] for _ in range(n)]



for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

def main(x,next):
      
     for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            
            if check[i][j]:
                continue
            print("print(data[i][j]) : ",data[i][j])
           
            main(x+1,i+1)
            check[i][j]=True

            return sum_all
        

main(0,0)

    