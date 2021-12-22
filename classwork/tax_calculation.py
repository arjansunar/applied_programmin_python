import datetime

output = '''
                        Income Tax Calculation System

                            Lazimpat. Kathmandu
____________________________________________________________________________________
    '''

current_date= datetime.date.today()
output+=f'\n\t\t\tWelcome to the income Tax Calculation System \t\t\t{current_date}'
output+="\n_____________________________________________________________________________\n"

print(output)

no_of_customer= int(input("Enter the number of customer: "))

name=[]
age=[]
address=[]
is_married=[]
income=[]

for i in range(no_of_customer):
    name.append(input(f'Enter your name[{i+1}]: ' ))
    address.append(input(f'Enter your address[{i+1}]: '))
    age.append(input(f'Enter your age:[{i+1}] '))
    
    is_married.append(input(f'Are you married or unmarried(y/n)[{i+1}]:: '))
    income.append(int(input(f'Enter the monthly income::[{i+1}] ')))
    print("________________________________________________________________________")

def get_tax_amount(amount,rate):
    return (amount*rate)/100

def tax_calc(income, min_taxable_income = 400000, phase_4_tax_range = 1300000):
    total_tax =0
    
    # if income is less than 4lakhs 50 thousand
    if (income <= min_taxable_income):
        total_tax += get_tax_amount(income,1)
    else:
        total_tax += get_tax_amount(min_taxable_income,1)

    # for additional 1 lakh
    add_tax_amt=income - min_taxable_income

    if(add_tax_amt > 0):
        if ( add_tax_amt <= 100000): 
            total_tax += get_tax_amount(add_tax_amt, 10)
        else: 
            total_tax += get_tax_amount(100000,10)

    # for additional 2 lakhs
    add_tax_amt -= 100000
    if (add_tax_amt > 0):
        if (add_tax_amt <= 200000): 
            total_tax += get_tax_amount(add_tax_amt, 20)
        else: 
            total_tax += get_tax_amount(200000,20)

    # for more than 750000
    add_tax_amt -= 200000
    if (add_tax_amt > 0):
        if (add_tax_amt <= phase_4_tax_range): 
            total_tax += get_tax_amount(add_tax_amt, 30)
        else: 
            total_tax += get_tax_amount(phase_4_tax_range,30)

    # for more than 2 million
    add_tax_amt = income - 2000000
    if (add_tax_amt > 0):
        total_tax += get_tax_amount(add_tax_amt,36)

    return total_tax

def tax_calc_for_married_person(income):
    return tax_calc(income, min_taxable_income= 450000, phase_4_tax_range= 1250000)


# test cases
# print("--------------------for married person---------------------")
# print(f'tax for 150000:: {tax_calc_for_married_person(150000)}, expected:: 1500' )
# print(f'tax for 450000:: {tax_calc_for_married_person(450000)}, expected:: 4500' )
# print(f'tax for 500000:: {tax_calc_for_married_person(500000)}, expected:: 9500' )
# print(f'tax for 550000:: {tax_calc_for_married_person(550000)}, expected:: 14500' )
# print(f'tax for 650000:: {tax_calc_for_married_person(650000)}, expected:: 34500' )
# print(f'tax for 750000:: {tax_calc_for_married_person(750000)}, expected:: 54500' )
# print(f'tax for 850000:: {tax_calc_for_married_person(850000)}, expected:: 84500' )
# print(f'tax for 2000000:: {tax_calc_for_married_person(2000000)}, expected:: 429500' )
# print(f'tax for 2500000:: {tax_calc_for_married_person(2500000)}, expected:: 609500' )

# print("--------------------for unmarried person---------------------")
# print(f'tax for 150000:: {tax_calc(150000)}, expected:: 1500' )
# print(f'tax for 450000:: {tax_calc(450000)}, expected:: 9000' )
# print(f'tax for 500000:: {tax_calc(500000)}, expected:: 14000' )
# print(f'tax for 550000:: {tax_calc(550000)}, expected:: 24000' )
# print(f'tax for 650000:: {tax_calc(650000)}, expected:: 44000' )
# print(f'tax for 750000:: {tax_calc(750000)}, expected:: 69000' )
# print(f'tax for 850000:: {tax_calc(850000)}, expected:: 99000' )
# print(f'tax for 2000000:: {tax_calc(2000000)}, expected:: 444000' )
# print(f'tax for 2500000:: {tax_calc(2500000)}, expected:: 624000' )

for i in range(no_of_customer):
    res_tax=0
    if (is_married[i].lower()=='y'):
        # print(f'income is :{income[i]}')
        res_tax = tax_calc_for_married_person((income[i])*12)
    else: 
        # print(f'income is :{income[i]}')
        res_tax = tax_calc((income[i])*12)
    output+=f'\nThe annual tax for {name[i]} of {age[i]} years old in {address[i]} is:: {res_tax} '
    print(f'The annual tax for {name[i]} of {age[i]} years old in {address[i]} is:: {res_tax} ')


f = open("./output.txt", "w")
f.write(output)