def solution(price, money, count):
    answer = -1
    
    check=0
    for i in range(1,count+1):
        check+=price*i
    
    if check > money:
        answer=check-money
    else:
        answer=0
    
    return answer