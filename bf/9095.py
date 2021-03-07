T=int(input())

#숫자 4부터 이전 3개의 개수를 모두 더한 수가 총 개수가 되는 것

input_list=[]


for _ in range(T):
    input_list.append(int(input()))


dp=[1,2,4]

for i in range(3,max(input_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in input_list:
    print(dp[i-1])