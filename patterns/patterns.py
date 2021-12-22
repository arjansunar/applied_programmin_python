# expected output
# *****
# *   *
# *   *
# *   *
# *****

def hollow_square(no_of_rows):
    for i in range(1,no_of_rows+1):
        if i ==1 or i == no_of_rows:
            print("*"*no_of_rows)
        else: 
            print("*"+ " "*(no_of_rows-2)+ "*")


def diagonal_hollow_square(rows,char="*"):
    for i in range(1,rows+1):
        if i ==1 or i == rows:
            print(char*rows)
        elif(i%2==0):
            print(char*(rows//2) +" "+char*(rows//2)) 
        elif(rows> 10):
            print(char*(rows//2-1)+" "+char+" "+char*(rows//2-1))
        else: 
            print(char*(rows//3)+" "+char+" "+char*(rows//3))

# hollow_square(8)
diagonal_hollow_square(103,'#')
