a=5
b=10

#using third varible 
print(f'a is {a} b is {b}.') 

c=a
a=b
b=c

print(f'a is {a} b is {b}.') 

#without using third variable

d=99
e=70

print(f'd is {d} e is {e}.') 

d += e
e = d-e
d -= e

print(f'd is {d} e is {e}.') 

d *= e
e = d/e
d /=e

print(f'd is {d} e is {e}.') 



