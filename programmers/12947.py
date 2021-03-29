#하샤드 수
def solution(x):
    
    k=sum(map(int, str(x)))
    
    if(x%k==0):
        return True
    else:
        return False