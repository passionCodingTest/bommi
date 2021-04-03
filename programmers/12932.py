def solution(n):
    answer = []
    
    reverse_n=list(str(n))
    
    int_n = list(map(int, reverse_n))
    
    answer=int_n[::-1]
    
    return answer