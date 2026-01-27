# Relational operators [<,>,<=,>=,==,!=]
# Assignment Operators [+=, -=, *=, /=, %=, //=, **=]
# Logical Operators [and, or, not]
# Bitwise Operators [&, |, !, >>, <<, ~]

# Special operators for python
# Membership Operators [in(if memeber give true), not in(if not a memeber give true)]
# Identity Operators  [is , is not]

'''  Membership Operators

a = "hello"
print("h" in a) 
print("b" in a)
print("h" not in a)
print("b" not in a)

b = [18, 29, 'abc'] #cannot check individual character from a list, check full string, c in b is flase, abc in b is true
print(29 in b)
print('abc' in b)
'''

#  Identity Operators

a = 10
b = 20
c = 10
print(a is b) 
print(a is c)
print(c is b)
print(id(a))  #id of a and c will be same. a and c will be getting reference of same memory block.
print(id(b))
print(id(c))

a =20
print(a is b) 
print(a is c)
print(c is b)
print(id(a))  #id of a and b will be same. a and b will be getting reference of same memory block.
print(id(b))
print(id(c))

