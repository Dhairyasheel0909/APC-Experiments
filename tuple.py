t=(1,2,3,4)

print(type(t))
print(id(t))
print(t)

l=list(t)
l.append(5)

m=tuple(l)

print(m)
print(type(m))
print(id(m))