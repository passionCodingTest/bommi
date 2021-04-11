def solution(phone_number):
    answer = ''
    
    phone=list(phone_number)
    phone_f=[]
    
    for i in range(0,len(phone)-4):
        phone_f.append("*")
    
    number=phone_f+phone[-4::]
    
    answer=''.join(number)
    
    return answer