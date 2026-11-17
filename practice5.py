'''
move all zeroes to one end
'''

num = int(input("Enter limit:"))
x = []
y = []
for i in range(num):
    ele = int(input())
    x.append(ele)

for i in x:
    if i != 0:
        y.append(i)
for i in x:
    if i == 0:
        y.append(i)

print(y)
