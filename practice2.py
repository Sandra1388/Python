'''
second largest element
'''

n = int(input("ENter limit:"))
x=[]
for i in range(n):
    a = int(input())
    x.append(a)

first = x[0]
second = 1

for i in range(n):
    if x[i] > first:
        second = first
        first = x[i]
    elif x[i] != first:
        if second == -1 and x[i] > second:
            second = x[i]

print(second)
