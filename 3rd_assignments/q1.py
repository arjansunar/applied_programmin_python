print("Developed By: Arjan Gahatraj Sunar\n")
# 1. Write a method in Python to read lines from a text file FILE.TXT and display those lines, which
# are starting with ‘y’ alphabet.

def read_line_with_y(filepath):
    with open(filepath) as f:
        for line in f:
            if line[0] != 'y': continue
            print(line)

read_line_with_y('./file.txt')