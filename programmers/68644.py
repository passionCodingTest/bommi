#두 개 뽑아서 더하기
from itertools import permutations

def solution(numbers):
    answer = []
    check= list(permutations(numbers, 2))
    
    for i in range(len(check)):
        if sum(check[i]) not in answer:
            answer.append(sum(check[i]))
            
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))