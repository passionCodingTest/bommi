def solution(arr):
    answer = []
    arr.remove(min(arr))
    
    if arr==[]:
        arr.append(-1)
    
    answer=arr     
    return answer