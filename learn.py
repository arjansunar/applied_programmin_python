marks1=marks2=name=address=sem=""

print("\tWelcome to sunway college Exam section software::")
print("----------------------------------------------------------------")

print("\tEnter the name::",end="\t")
name=input()

print("\tEnter the address::",end="\t")
address=input()

print("\tEnter the sem::",end="\t")
sem=input()

print("\tEnter the marks of applied programming::",end="\t")
marks1=int(input())

print("\tEnter the marks of big data::",end="\t")
marks2=int(input())

print("-----------------------------------------------------------------------------")
print("\t\tSunway Int. College\n\t\tMaitidevi Kathmandu")
print("-----------------------------------------------------------------------------")

avg= (marks2+marks1)/2

print("-----------------------------------------------------------------------------\n")
print(f'Student Name: \t{name}\t\t\tSem-{sem}\nAddress: \t{address}\t\t\tRollNo=21009')
print("-----------------------------------------------------------------------------")


print(f'1. Applied programming\t{marks1}\n2. Big data\t{marks2}')
print(f'-----------------------------------------------------------------------------\nAverage: \t{avg}')
print("-----------------------------------------------------------------------------")
print(f'The student {name} got {avg}%.')
print("-----------------------------------------------------------------------------")

division=""

if(avg >80): division= "distinction"
elif (avg > 70 ): division ="first" 
elif (avg> 60): division="Second"
else: division = "fail"

print(f'Division: \t{division}')
