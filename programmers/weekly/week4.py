def solution(table, languages, preference):
    answer = ''
    cnt=len(table)
    
    dict_score={}
    score={}
    
    for i in range(0,cnt):
        table[i]=table[i].split(',')
        table[i][0]=table[i][0].split(" ")
    
    for i in range(len(languages)):
        dict_score[languages[i]]=preference[i]
    
    for j in table:
        j[0].reverse()
        for k in range(0,len(j[0])-1):
            if j[0][k] in dict_score:
                key=j[0][len(j[0])-1]
                value=(k+1)*dict_score[j[0][k]]
                
                if key in score:
                    score[key]= [score[key][0] + value]
                else:
                    score[key] = [value]
                    
    
    max_value=max(score.values())
    d=dict((key,value) for key, value in score.items() if value == max_value)
    answer=sorted(d,key = lambda x: x[0])[:1][0]
    
    
    return answer