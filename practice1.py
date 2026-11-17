'''
Given a string, find the first non-repeating character and print it.
'''

s = input()
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
