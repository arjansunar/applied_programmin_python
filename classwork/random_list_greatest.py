import random

def create_random_list(length,start,end):
    return [random.randint(start,end) for i in range(length)]

length = int(input("Enter the length of the array: "))
start = int(input("Enter the random start values: "))
end = int(input("Enter the random end values: "))

arr = create_random_list(length,start,end)
print("\nThe list is:",arr)

def get_greatest_num(arr):
    if(len(arr) <= 0 ): return
    greatest = arr[0]
    for i in arr:
        if greatest < i:
            greatest = i
    return greatest

print("\nThe greatest value is: ", get_greatest_num(arr))