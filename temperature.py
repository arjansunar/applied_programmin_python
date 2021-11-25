
def conditionals(temp):
    if temp  > 85: return "very hot"
    elif temp >= 60: return "pleasant day" 
    elif temp < 60:  return "very cold"
    else: return "error: wrong input"

no_of_days= int(input("How many days to record?  "))
print(f'Please enter {no_of_days} days temperature readings..')
days= []

for i in range(no_of_days):
    days.append(int(input(f'Temperature day [{i+1}] = ')))

for ind,val in enumerate(days):
    print(f'The day {ind+1} was {conditionals(val)}')
