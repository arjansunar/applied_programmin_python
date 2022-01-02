# 3. Write a program that asks the user for the name of a file. The program should read all of the file’s
# data into a list and display the number of lines of data that the file contains, and then ask the user to
# enter the number of the line that he or she wants to view. The program should display the specified
# line.
# The program should handle the following exceptions by displaying an error message:
# • IOError exceptions that are raised when the specified filename cannot be found or opened.
# • ValueError exceptions that are raised when a non-integer value is given as a line number.
# • IndexError exceptions that are raised when the line number is outside the range of the
# data list.

file_name =  input("Enter the name of the file: ")

try:
    f = open(file_name)
    file_list =  list(f)
    print(f'The file has {len(file_list)} lines') 
    line_no = int(input("Enter the line number: "))
    if line_no < 0: raise IndexError
    print(f'\nLine no [{line_no}]: {file_list[line_no-1]}')
except IndexError:
    print("Line number out of range")
except ValueError:
    print("Non-integer value as a line number")
except IOError:
    print("File not found")