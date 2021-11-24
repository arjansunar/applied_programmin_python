# func to get sum of digits of a given integer
def get_sum_of_digits(num):
    sum =0
    while num > 0:
        sum += num % 10
        num //=10
    return sum

# func to get sum of digits of a given integer recursively
def get_sum_digits_recursive(num):
    if num <= 1:
        return 0
    return num % 10 + get_sum_digits_recursive(num//10)  

# func to find odd or even digits in a number
def find_even_or_odd_digits(num):
    while num > 0: 
        rem = num % 10
        if rem % 2==0:
            print(f'{rem} is even')
        else:
            print(f'{rem} is odd')
        num//=10

num = int(input("enter a number: "))
print(f'The sum of the digits is {get_sum_digits_recursive(num)}')
print(f'The odality of the digits are: \n')
find_even_or_odd_digits(num)
