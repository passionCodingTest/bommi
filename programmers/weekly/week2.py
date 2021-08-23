import numpy as np

#nparray로 2차원 배열 만들어서 자신이 입력한 숫자만가져오도록 함

def solution(scores):
    answer = ''        # 정답 문자열 저장
    scores=np.array(scores).reshape(len(scores),len(scores))
    student=[]
    
    
    for idx in range(len(scores)):
        student=scores[:,idx]
        
        for value in student:
            if value < 0 or value > 100:
                student = np.delete(student, np.where(student == value))
        # 가장 높고 낮은 점수를 저장
        max_value = student.max()
        min_value = student.min()

        # 가장 높고 낮은 점수의 개수를 저장
        max_cnt = len(student[student == max_value])
        min_cnt = len(student[student == min_value])

        # 가장 높고 낮은 점수가 자신이 매긴 점수이면서,
        # 그 점수의 개수가 1개일 경우 제외
        if student[idx] == max_value and max_cnt == 1:
            student =np.delete(student, idx)
        elif student[idx] == min_value and min_cnt == 1:
            student =np.delete(student, idx)

        # 학생의 점수 평균을 계산한 다음 최종 학점 반영
        total = sum(student) / len(student)
        if total >= 90:
            answer += "A"
        elif 80 <= total < 90:
            answer += "B"
        elif 70 <= total < 80:
            answer += "C"
        elif 50 <= total < 70:
            answer += "D"
        else:
            answer += "F" 
            
    return answer