n = int(input())
for i in range(n):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*", end=" ")
    print()