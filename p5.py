'''
Python Containers [storage devices]
---------------
1) List [no need to specify size, It is a homogeneous or hetrogeneous collection of elements, Mutable]
2) Tuple [Immutable]
3) Dictionary [Data is stored in key value payer]
4) Set [collection of unique elements, no order]

Representation
-------------
List:-       a = []
Tuple:-      b = ()
Dictionary:- {key:value}, {"abc":45}, {45:"hai"}, 
             we can access data by using key eg:x={23:89}, print(x[23])
'''

'''
a=[10,20,30]
print(a[1])
a[1]=200
print(a[1]) #chnaged the value at a[1] to 200
'''

a=[20,30,40,50,60,70,80]

print(a[1:3])    # 1:-start index, 3:-end index. prints 1,2 index values

print(a[0:4:2])  # s:- step, increment by 2

print(a[:])      # prints full list

print(a[4:0:-1]) # prints from 4 to 1

print(a[::-1])   # reverse 
