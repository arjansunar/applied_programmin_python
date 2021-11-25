use_sentence=input("Enter a sentence...") 
vowel_cnt={
        'a':0,
        'e': 0,
        'i':0,
        'o':0,
        'u':0
     }

def is_prime(num):
    if (num <=1): return False
    if (num == 2): return True
    for i in range(2,num//2+1):
        if (num % i ==0): return False
    return True

for i in use_sentence:
    if(i.lower() == 'a'):
        vowel_cnt['a']+=1
    elif(i.lower() == 'e'):
        vowel_cnt['e']+=1
    elif(i.lower() == 'i'):
        vowel_cnt['i']+=1
    elif(i.lower() == 'o'):
        vowel_cnt['o']+=1
    elif(i.lower() == 'u'):
        vowel_cnt['u']+=1
    else: 
        continue

print(vowel_cnt)

for key,val in vowel_cnt.items():
    if(is_prime(val)):
        print(f'The count for {key} is prime')
    else: 
        print(f'The count for {key} is not prime')