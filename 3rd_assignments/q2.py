def write_to_file(filepath,output):
    with open(filepath,'w') as f:
        f.write(output)

def get_user_text():
    usr_input =''
    print("Write the text content: (Type   '!exit' to continue)")
    while True: 
        temp =''
        temp  += input()
        if ('!exit' == temp): 
            break
        usr_input += temp +'\n'
    return usr_input 

write_to_file('./output.txt', get_user_text())