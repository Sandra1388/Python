n = int(input())
temp = n
sm = 0
rev = 0
power = len(str(n))
while n!= 0:
    i = n%10
    sm =  sm + i ** power
    n = n//10
    
if temp == sm:
    print("amstrong")
else:
    print("Not amstrong")
