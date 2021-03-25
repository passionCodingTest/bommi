#2016년

def solution(a, b):
    day_list = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ''

    total_day = 0

    for i in range(0, a-1):
        total_day += month_list[i]

    total_day += b-1;

    answer = day_list[total_day%7]

    return answer