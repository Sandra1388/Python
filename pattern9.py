n = int(input())
letters = ['A', 'B', 'C', 'D', 'E','F','G','H']

for i in range(1, n + 1):
    for j in range(i):
        print(letters[j], end=" ")
    print()
