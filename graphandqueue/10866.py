from sys import stdin 
import collections
queue=[]
collections.deque(queue) 

for _ in range(int(stdin.readline())): 
    arr = stdin.readline().split()

    if arr[0] == 'push_front': 
        queue.insert(0,arr[1]) 

    elif arr[0] == 'push_back': 
        queue.append(arr[1]) 
    
    elif arr[0] == 'pop_front':
        if queue: print(queue.pop(0)) 
        else:
            print(-1)
         
    elif arr[0] == 'pop_back':
        if queue: print(queue.pop(-1)) 
        else:
            print(-1) 
         
    
    elif arr[0] == 'size': 
        print(len(queue))
    
    elif arr[0] == 'empty': 
        if queue: print(0) 
        else: print(1)

    elif arr[0] == 'front': 
        if queue: print(queue[0]) 
        else: print(-1) 

    elif arr[0] == 'back': 
        if queue: print(queue[-1]) 
        else: print(-1)  
    
    else: pass

