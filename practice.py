n = int(input("Enter limit:"))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

c = 0
new = 0

for i in range(n):
    if arr[i] == 1:
        c = 1
    for j in range(i+1):
        if arr[j] == 1:
            c += 1
            break
    if c >= new:
        new = c
print(new)
