# wap a program to take random value and check the value is 2 or 3 multiple and if 2 multiple then print the table of its 

import random
range_val = int(input("Enter the range for random value: "))

random_val=  random.randint(1,range_val)


def get_table(val):
    if ( val % 3 == 0): 
        print(f'{val} is odd')
        return
    else: 
        print(f'The table for {val}')
        for i in range(1,10):
            print(f'{val} x {i} = {val * i}')
    
get_table(random_val)
    

