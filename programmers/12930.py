def solution(s):
    answer = ''
    
    word=s.split(" ")
    
    
    for i in word:
        for idx,n in enumerate (i):
            
            if(idx%2==0):
                answer += n.upper()
            
            elif(idx%2==1):
                answer += n.lower()
                
        answer += " " 
    
    
    return answer[:-1]