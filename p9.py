'''
Write a program to get N, the size of the array in first line of input. Then get N elements from user as input.

Rearrange the elements of the array such that all even elements comes in the front of the array and then all the odd elements after it.
'''
n = int(input())
a = list(map(int, input().split()))
e=[]
o=[]
n=[]
for i in a:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
e.extend(o)
for i in e:
    print(i, end=" ")
   
    