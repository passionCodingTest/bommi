egg = [1, 1]
d = [0, 0]
bd = [0, 0, 0, 0, 0]
n = int(input())
for i in range(2,n+1):#2,7
    if i > 4:
        bd.append(bd[i-4] + d[i-4])
    egg.append(egg[i-1] + d[i-1] - bd[i])
    d.append(egg[i-2] + d[i-2] - bd[i])
print(bd)
print(d)
print(egg)

print(d[n]+egg[n]+bd[n])