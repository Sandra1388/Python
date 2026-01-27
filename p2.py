# Read values form keyboard
# by using input() it takes data as strings even if it is a number. So use typecasting [int(input)]
a = int(input())
b = int(input())

sum = a + b
d = b / a #division in python is float division
dd = b // a #gives integer quotient only

print("sum =", sum)
print("Difference =", a - b)
print("Product =", a * b)
print("Division =", d)
print("Division =", dd)


