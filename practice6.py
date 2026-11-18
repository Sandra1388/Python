'''
longest word in a sentence
'''

se = input()
s = se.split()

long = s[0]

for i in s:
    if len(i) > len(long):
        long = i

print(long)

