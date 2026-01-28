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