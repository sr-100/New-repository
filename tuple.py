x=[]
x=(1,2,3,4)
print(x)
print(x(x))







x=(1,2,3,4)
x=[1,2,3,4]
print('list is:',x)
print(type(x))
#append
x.append(5)
print(x)
#extend
x.extend([3,6,9])
print(x)
print(len(x))
print(x.count(3))
#insert
print(x[2])
x.insert(4,16)
print(x)
print('sum of x is:',sum(x))
print('maximum element of x:',max(x))
print('minimum value of x is:',min(x))
#copy
lis=x.copy()
x.append(9)
print(lis)
print(x)
#slicing
print(x[0:3])
#sort
x.sort()
print(x)
x.reverse()
print(x)
#delete
del x[2]
print(x)
x.pop()
print()
x.pop(4)
print(x)
x.remove(3)
print(x)
x.clear()
print(x)


