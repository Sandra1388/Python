'''
Write a program to count the occurrences of a given character in a string.
The character and string are entered using the main function.
You need to write the code to find the number of times the given character occur in the given string and return the number.
'''
def function(text):
    s = text[0]
    c=0
    for i in range(1, len(text)):
        if(s is text[i]):
            c = c+1
    return c
text = input()
count = function(text)
print(count)