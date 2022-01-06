class Tax_calc:
    
    @staticmethod
    def get_tax_amount(amount,rate):
        return (amount*rate)/100

    @staticmethod
    def tax_calc( income, min_taxable_income = 400000, phase_4_tax_range = 1300000):
        total_tax =0
        
        # if income is less than 4lakhs 50 thousand
        if (income <= min_taxable_income):
            total_tax += Tax_calc.get_tax_amount(income,1)
        else:
            total_tax += Tax_calc.get_tax_amount(min_taxable_income,1)

        # for additional 1 lakh
        add_tax_amt=income - min_taxable_income

        if(add_tax_amt > 0):
            if ( add_tax_amt <= 100000): 
                total_tax += Tax_calc.get_tax_amount(add_tax_amt, 10)
            else: 
                total_tax += Tax_calc.get_tax_amount(100000,10)

        # for additional 2 lakhs
        add_tax_amt -= 100000
        if (add_tax_amt > 0):
            if (add_tax_amt <= 200000): 
                total_tax += Tax_calc.get_tax_amount(add_tax_amt, 20)
            else: 
                total_tax += Tax_calc.get_tax_amount(200000,20)

        # for more than 750000
        add_tax_amt -= 200000
        if (add_tax_amt > 0):
            if (add_tax_amt <= phase_4_tax_range): 
                total_tax += Tax_calc.get_tax_amount(add_tax_amt, 30)
            else: 
                total_tax += Tax_calc.get_tax_amount(phase_4_tax_range,30)

        # for more than 2 million
        add_tax_amt = income - 2000000
        if (add_tax_amt > 0):
            total_tax += Tax_calc.get_tax_amount(add_tax_amt,36)

        return total_tax

    @staticmethod
    def tax_calc_for_married_person( income):
        return Tax_calc.tax_calc(income, min_taxable_income= 450000, phase_4_tax_range= 1250000)
    
    
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
 
name= address= is_married= ""
age=income= 0


name=(input(f'Enter your name: ' ))
address=(input(f'Enter your address: '))
age=int(input(f'Enter your age: '))
is_married=(input(f'Are you married or unmarried(y/n):: '))
income=(int(input(f'Enter the monthly income:: ')))
print("________________________________________________________________________")



res_tax=0
if (is_married.lower()=='y'):
    # print(f'income is :{income[i]}')
    res_tax = Tax_calc.tax_calc_for_married_person(income=(income)*12)
else: 
    # print(f'income is :{income[i]}')
    res_tax = Tax_calc.tax_calc(income=(income)*12)
output+=f'\nThe annual tax for {name} of {age} years old in {address} is:: {res_tax} '
print(f'The annual tax for {name} of {age} years old in {address} is:: {res_tax} ')

