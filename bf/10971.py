n = int(input())

mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))

def next_permutation(lst):
    n = len(lst)
    i = n - 1
    while i > 0 and lst[i - 1] >= lst[i]:
        i -= 1
    if i == 0:
        return [-1]
    j = n - 1
    while lst[i - 1] >= lst[j]:
        j -= 1
    tmp = lst[j]
    lst[j] = lst[i - 1]
    lst[i - 1] = tmp

    lst = lst[:i] + sorted(lst[i:])
    return lst

pathes = []

path = [i for i in range(2, n + 1)]
while True:
    if path == [-1]:
        break
    pathes.append([1] + path)
    path = next_permutation(path)


ans = 999999999
for path in pathes:
    total = 0
    flag = False
    for i in range(len(path) - 1):
        cost = mat[path[i] - 1][path[i + 1] - 1]
        if cost == 0:
            flag = True
            break
        total += cost
    cost = mat[path[-1] - 1][0]
    if cost == 0 or flag:
        continue
    total += cost
    ans = min(total, ans)
print(ans)