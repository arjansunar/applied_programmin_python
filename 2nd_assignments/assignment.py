print('''
    Developed by Arjan Gahatraj Sunar
=========================================    
    ''')

# q1
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********

# for i in range(1,9):
#     print("*"*i)

# q2 Write a program that asks the user to enter the number of times that they have run around
# a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.
# When the loop finishes, the program should display the time of their fastest lap, the time of
# their slowest lap, and their average lap time.

# no_of_laps = int(input("Enter the number of laps:: "))
# lap_time=[]
# for i in range(no_of_laps):
#     lap_time.append(int(input(f'Enter the time for lap no {i+1} in minutes:: ')))

# lap_time.sort()

# print(f'The fastest lap time is:: {lap_time[0]}')
# print(f'The slowest lap time is:: {lap_time[no_of_laps-1]}')

# def get_avg(lap_times): 
#     sum = 0
#     for i in lap_times:
#         sum += i
#     return sum/len(lap_times)

# avg_lap_time= get_avg(lap_time)

# print(f'The average lap time is:: {avg_lap_time}')

# q3 driver license office application

correct_ans=["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]

passing_file = open("2nd_assignments/passing_test_case.txt")
failing_file = open("2nd_assignments/failing_test_case.txt")


def file_to_list(file):
    return file.readlines()

def ans_checker(list_of_ans,correct_ans):
    cnt=0
    incorrect_questions=[]
    for i in list_of_ans:
        # print(f'ans {ans[cnt]} file:: {i}')
        if (correct_ans[cnt] != i.strip()):
            incorrect_questions.append(cnt+1)
        cnt+=1
    return incorrect_questions

def create_output(file,ans):
    list_of_ans= file_to_list(file)
    incorrect_questions = ans_checker(list_of_ans,ans)
    no_of_wrong_ans = len(incorrect_questions)
    print(f'Student has {"passed" if ( no_of_wrong_ans <= 5) else "failed"}',end="\n\n")
    print(f'Total number of correct answers:: { 20 - no_of_wrong_ans}',end="\n\n") 
    if(no_of_wrong_ans > 0):
        print(f'Questions answered wrong::',end="  [ ")
        print(*incorrect_questions, sep=", ",end=" ]\n\n")
    print('================================================')


print("Passing test case:: ",end="\n\n")
create_output(passing_file,correct_ans)

print("Failing test case:: ",end="\n\n")
create_output(failing_file,correct_ans)


passing_file.close()
failing_file.close()