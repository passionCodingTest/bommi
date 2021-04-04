def solution(n):
    list_N = str(n)
    answer = 0
    for i in range(len(list_N)):
        answer += int(list_N[i])
    return answer