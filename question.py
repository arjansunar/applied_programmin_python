import cmath
import random
def get_area_of_triangle(a,b,c):
    s= (a+b+c)/2
    return cmath.sqrt(s*(s-a)*(s-b)*(s-c)).real

def solve_quadratic_eqn(a,b,c):
    d= b**2 - 4*a*c
    x1= (-b - cmath.sqrt(d))/(2*a)
    x2= (-b + cmath.sqrt(d))/(2*a)
    return [x1,x2]

def get_random_variable(start,end):
    return random.randint(start,end)
    
def is_even(val:int):
    return val % 2 == 0 

print(f'the area of trangle is {get_area_of_triangle(5,6,7)}')
print(f'the solution of quadratic equation is {solve_quadratic_eqn(1,0,4)}')

random_val= get_random_variable(1,10)
result= "even" if  is_even(random_val % 5) else "odd"
print(f'the 5 modulo of random value : {random_val} is {result}')



