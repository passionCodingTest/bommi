def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(signs)):
        if signs[i]==False:
            answer+=absolutes[i]*(-1)
        else:
            answer+=absolutes[i]
    
    return answer