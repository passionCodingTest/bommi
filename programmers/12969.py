#직사각형 별찍기

n, m = map(int, input().strip().split(' '))
for i in range(m):            
    for j in range(n):        
        print('*', end='') 
    print()


#a, b = map(int, input().strip().split(' '))
#answer = ('*'*a +'\n')*b
#print(answer)