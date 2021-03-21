#문자열 내 p와 y의 개수

def solution(s):
    answer = True
    
    s=s.lower()
    a=s.count('p')
    b=s.count('y')
    
    if a==b:
        return answer
    else:
        return False
    
    return True
