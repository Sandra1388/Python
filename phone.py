num = list(map(int, input().split()))
d = {}
m = 0
for i in num:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in set(num):
    if d[i] > m:
        m = d[i]
        new = i
print(new)
