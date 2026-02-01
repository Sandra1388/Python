'''
Check if the given string is palindrome or not.

Return 1 if the string is palindrome.

Return 0 if the string is not palindrome.
'''
def function(var):
    s = var[::-1]
    if(s == var):
        return 1
    else:
        return 0

text = input()
out = function(text)
print(out)